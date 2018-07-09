# coding=utf-8
import requests
from parsel import Selector
import pandas as pd
import time

#############################################################
''''' 
爬取链家网的二手房信息
'''

###########################################################
# 需要爬取的区县
areas = ['pudong','minhang','baoshan','xuhui','putuo','yangpu','changning','songjiang','jiading','huangpu', \
        'jingan','zhabei','hongkou','qingpu','fengxian','jinshan','chongming','shanghaizhoubian']


# 进行网络请求的浏览器头部
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'
}

# pages是不同页码的网址列表
# pages = ['https://sh.lianjia.com/ershoufang/{}/pg{}/'.format(area, x) for area in areas for x in range(1, 100)]
############################################################

#############################################################
# 标注每一列信息
lj_sh = pd.DataFrame(columns=['title', '总价', '均价', '小区名',\
                       '区域1', '区域2', '房屋户型', '所在楼层', '建筑面积', '户型结构', \
                       '套内面积', '建筑类型', '房屋朝向', '建筑结构', '装修情况', '梯户比例',\
                        '配备电梯', '产权年限', '挂牌时间', '交易权属', '上次交易', '房屋用途',\
                         '房屋年限', '产权所属', '抵押信息', '房本备件', '特色标签','卖点'])


# 这个函数是用来获取一个主页面上链家网二手房的信息
def l_par_html(url):
    # 根据url获取获取主页面
    html = requests.get(url, headers=headers, stream=True)
    sel = Selector(html.text)

    # 解析主页面，获取主页面中各个房源的url
    new_urls = sel.xpath('//li[@class="clear"]/a/@href').extract()

    # 根据各个房源的url，进入页面进行爬取
    pages_info_ = []
    for new_url in new_urls:
        new_html = requests.get(new_url,headers=headers,stream=True)
        new_sel = Selector(new_html.text)

        try:
          #爬取房源title
          title = new_sel.xpath\
                  ('//div[@class="sellDetailHeader"]/div/div/div/h1//text()').extract()
          title_column = ["title"]

          #爬取房源总价/均价(first)，小区名（second），区域（third）
          profile_first = new_sel.xpath\
                          ('//div[@class="overview"]/div[@class="content"]\
                            /div[@class="price "]//text()').extract()
          profile_second = new_sel.xpath\
                          ('//div[@class="overview"]/div[@class="content"]\
                            /div[@class="aroundInfo"]/div[@class="communityName"]\
                            /a[@class="info "]//text()').extract()
          profile_third = new_sel.xpath
                          ('//div[@class="overview"]/div[@class="content"]\
                            /div[@class="aroundInfo"]/div[@class="areaName"]\
                            /span[@class="info"]//text()').extract()
          profile = [profile_first[0],profile_first[2],\
                    profile_second[0],profile_third[0],profile_third[2]]
          profile_column = ["总价","均价","小区名","区域1","区域2"]


          #爬取房源基本信息
          basic_information_first = new_sel.xpath\
                              ('//div[@id="introduction"]/div/div/div/div[@class="content"]/ul/li//text()').extract()
          basic_information_second = [i.strip() for i in basic_information_first]
          basic_information_third = [i for i in basic_information_second if i != '']
          basic_information_column = []
          basic_information = []
          for i in basic_information_third:
            if(basic_information_third.index(i) % 2 == 0):
                basic_information_column.append(i)
            else:
                basic_information.append(i)

          #爬取房源特色标签
          house_feature_label_first = new_sel.xpath\
                            ('//div[@class="introContent showbasemore"]/div[@class="tags clear"]/div[@class="content"]//text()').extract()
          house_feature_label_second = [i.strip() for i in house_feature_label_first]
          house_feature_label_third = [i for i in house_feature_label_second if i != '']
          house_feature_label = [''.join([i + ' ' for i in house_feature_label_third])]
          house_feature_label_column = ["特色标签"]

          #爬取卖点
          house_feature_first = new_sel.xpath\
                            ('//div[@class="introContent showbasemore"]/div[@class="baseattribute clear"]//text()').extract()
          house_feature_second = [i.strip() for i in house_feature_first]
          house_feature_third = [i for i in house_feature_second if i != '']
          house_feature = [''.join([i + ' ' for i in house_feature_third])]
          house_feature_column = ["卖点"]

          # 将上述信息合并为一条信息
          dataframe = title + profile + basic_information + house_feature_label + house_feature
          #dataframe_column = title_column + profile_column + basic_information_column + house_feature_label_column + house_feature_column

          print(dataframe)

          # 将信息转为dataFrame形式，便于存入文件中
          pages_info_.append(dataframe)
          pages_info = pd.DataFrame(pages_info_, columns=['title', \
                  '总价', '均价', '小区名', '区域1', '区域2', '房屋户型',\
                   '所在楼层', '建筑面积', '户型结构', '套内面积', '建筑类型',\
                    '房屋朝向', '建筑结构', '装修情况', '梯户比例', '配备电梯', \
                    '产权年限', '挂牌时间', '交易权属', '上次交易', '房屋用途',\
                     '房屋年限', '产权所属', '抵押信息', '房本备件', '特色标签','卖点'])
        except IndexError:
            pass
        except AssertionError:
            pass

    return pages_info


# 根据网页url规则生成主页面url，调用函数进行爬取
for area in areas:
    for pg in range(1, 101):
        print("area: ", area, " page: ", pg, "\n")
        page = 'https://sh.lianjia.com/ershoufang/{}/pg{}/'.format(area, pg)
        a = l_par_html(page)
        lj_sh = pd.concat([lj_sh, a], ignore_index=True)

# 将表格数据输出到excel文件
lj_sh.to_excel('/Users/dmzxwcy0112/Desktop/house_info.xlsx')