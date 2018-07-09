import pandas as pd
import re
import random
import xlrd
import openpyxl

'''
  标签   数值类型
①总价     数值型
②区域1    字符型，包括"宝山""崇明""奉贤""虹口""黄浦""嘉定""金山""静安""闵行""浦东""普陀""青浦""上海周边""松江""徐汇"
                    "杨浦""闸北""长宁"
③房屋户型  字符型，格式为"x室x厅x厨x卫"，x为数字
④所在楼层  字符列表，包括["低"，"低"]["低"，"中"]["低"，"高"]["中"，"低"]["中"，"中"]["中"，"高"]["高"，"低"]["高"，"中"]["高"，"高"]
⑤建筑面积  数值型
⑥建筑类型  字符型，包括"板楼""塔楼"
⑦房屋朝向  数值列表："东": 0, "南": 1, "西": 2, "北": 3, "东南": 4, "西北": 5, "东北": 6, "西南": 7（未知数据补为 南(1)）
            例：[0]表示房屋朝向为东，[0，2]表示房屋朝东且朝西
⑧建筑数据  字符型，包括"钢混结构""砖混结构"
⑨装修情况  字符型，包括"简装""精装""毛坯""其他"
⑩梯户比例  数值型，由x/y得到，x梯y户
⑪配备电梯  字符型，包括"有""无""暂无数据"
⑫房屋用途  字符型，包括"花园洋房""旧式里弄""老公寓""普通住宅""旧式里弄"
⑬房本备件  字符型，包括"未上传房本照片""已上传房本照片"
⑭卖点     字符型，包括"交通便利""未说明"
'''

common_used_numerals_tmp = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, \
                            '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}


# 中文数字转换为阿拉伯数字
def chinese2digits(uchars_chinese):
    total = 0
    r = 1  # 表示单位：个十百千...
    for i in range(len(uchars_chinese) - 1, -1, -1):
        val = common_used_numerals_tmp.get(uchars_chinese[i])
        if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
            if val > r:
                r = val
                total = total + val
            else:
                r = r * val
                # total =total + r * x
        elif val >= 10:
            if val > r:
                r = val
            else:
                r = r * val
        else:
            total = total + r * val
    return total

# 删除无用行列
def delete_column_row(data_raw, col):
    data_raw = data_raw.drop(data_raw.columns[col], 1)

    for i in data_raw.index:
        if "简装" in data_raw.loc[i, "房屋朝向"] or "精装" in data_raw.loc[i, "房屋朝向"] or "毛坯" in data_raw.loc[i, "房屋朝向"] or "70年" in data_raw.loc[i, "装修情况"] or "抵押" in data_raw.loc[i, "房屋用途"] or "0" in data_raw.loc[i, "梯户比例"]:
            data_raw = data_raw.drop([i])

    return data_raw


''' 处理"所在楼层"列
    最终值为["低"，"低"]["低"，"中"]["低"，"高"]["中"，"低"]["中"，"中"]["中"，"高"]["高"，"低"]["高"，"中"]["高"，"高"]
    前者是用户所在楼层相对于整栋楼的位置，后者是整个楼的情况：低于6及刚好6层属于低，低于12层及刚好12层属于中，低于300层属于高，可能存在
        空值，补全为低
'''
def floor_filter(data_raw):
    for i in data_raw.index:
        usr = data_raw.loc[i, "所在楼层"][0:1]
        total = re.findall(r"\d+", data_raw.loc[i, "所在楼层"])
        total = int(total[0])
        if total <= 6:
            total = "低"
        elif total <= 12:
            total = "中"
        elif total < 300:
            total = "高"
        else:
            total = "低"
        data_raw.at[i, "所在楼层"] = [usr, total]

    return data_raw


# 处理建筑面积，最终剩下数值
def area_filter(data_raw):
    for i in data_raw.index:
        data_raw.loc[i, "建筑面积"] = data_raw.loc[i, "建筑面积"].replace("㎡", "")

    # data_raw["建筑面积"] = data_raw["建筑面积"].astype("float")
    return data_raw


# 处理建筑类型，最终数值包括：板楼，塔楼, 未知数据被补全为板楼
def type_filter(data_raw):
    for i in data_raw.index:
        if data_raw.loc[i, "建筑类型"] == "暂无数据":
            data_raw.loc[i, "建筑类型"] = "板楼"

    return data_raw


# 处理房屋朝向，最终为数值列表："东": 0, "南": 1, "西": 2, "北": 3, "东南": 4, "西北": 5, "东北": 6, "西南": 7（未知数据补为 向南）
# 例：[0]表示房屋朝向为东，[0，2]表示房屋朝东且朝西
def face_filter(data_raw):
    face_dic = {"东": 0, "南": 1, "西": 2, "北": 3, "东南": 4, "西北": 5, "东北": 6, "西南": 7}
    for i in data_raw.index:
        face_dat = data_raw.loc[i, "房屋朝向"].split(' ')
        face_dat = [face_dic.get(fac, 1) for fac in face_dat]
        data_raw.at[i, "房屋朝向"] = face_dat

    return data_raw


''' 处理建筑结构
    最终值为"钢混结构""砖混结构"
    若为未知结构，则根据楼层信息，若属于矮楼(低楼)，则补全为砖混结构
                              若属于中高楼，则补全为钢混结构
'''
def struc_filter(data_raw):
    for i in data_raw.index:
        if data_raw.loc[i, "建筑结构"] == "未知结构":
            if data_raw.loc[i, "所在楼层"][1] == "低":
                data_raw.loc[i, "建筑结构"] = "砖混结构"
            else:
                data_raw.loc[i, "建筑结构"] = "钢混结构"

    return data_raw


''' 处理梯户比例
    使用chinese2digits()函数将字符串中的中文数字转化成阿拉伯数字,x梯y户
    再将x/y作为最后的数值类型
'''
def elev_filter(data_raw):
    for i in data_raw.index:
        elev_dat = re.split('[梯户]', data_raw.loc[i, "梯户比例"])
        elev_dat = [chinese2digits(i) for i in elev_dat]
        data_raw.loc[i, "梯户比例"] = round(elev_dat[0] / elev_dat[1],2)

    return data_raw

''' 处理配备电梯
    最终值为"有""无"
    若为暂无数据，则根据楼层信息，若属于矮楼(低楼)，则补全为有电梯
                                若属于中高楼，则补全为无电梯
'''

def hase_filter(data_raw):
    for i in data_raw.index:
        if data_raw.loc[i, "配备电梯"] == "暂无数据":
            if data_raw.loc[i, "所在楼层"][1] == "低":
                data_raw.loc[i, "配备电梯"] = "无"
            else:
                data_raw.loc[i, "配备电梯"] = "有"
    
    return data_raw

''' 处理距离问题
    若在特色标签中含"地铁"，或者在卖点中含"地铁""交通""线""路""近"等字样的，最后的字符串为"交通便利"
    否则最后返回的字符串为"未说明"
'''
def dist_filter(data_raw):
    for i in data_raw.index:
        dist_label = str(data_raw.loc[i, "特色标签"]).split(' ')
        #print(type(data_raw.loc[i, "卖点"]))
        if "地铁" in dist_label or \
           "地铁" in str(data_raw.loc[i, "卖点"]) or \
            "交通" in str(data_raw.loc[i, "卖点"]) or \
            "线" in str(data_raw.loc[i, "卖点"]) or \
            "路" in str(data_raw.loc[i, "卖点"]) or \
            "近" in str(data_raw.loc[i, "卖点"]):
            data_raw.loc[i, "卖点"] = "交通便利"
        else:
            data_raw.loc[i, "卖点"] = "未说明"

    data_raw = data_raw.drop(data_raw.columns[-2], 1)
    return data_raw



def main():
    pd.set_option('max_colwidth', 20)

    # 读取源文件
    data_raw = pd.read_excel(r'D:\house_info.xlsx')

    # 删除无用行列
    # col = [0, 2, 3, 5, 9, 10, 17, 18, 19, 20]
    col = [0, 2, 3, 5, 9, 10, 17, 18, 19, 20, 22, 23, 24]
    data_raw = delete_column_row(data_raw, col)

    # 处理所在楼层
    data_raw = floor_filter(data_raw)

    # 处理建筑面积
    data_raw = area_filter(data_raw)

    # 处理建筑类型
    data_raw = type_filter(data_raw)

    # 处理房屋朝向
    data_raw = face_filter(data_raw)

    # 处理建筑结构
    data_raw = struc_filter(data_raw)

    #处理梯户比例
    data_raw = elev_filter(data_raw)
    
    #处理配备电梯
    data_raw = hase_filter(data_raw)

    # 处理距离问题
    data_raw = dist_filter(data_raw)

    data_raw.to_excel(r'C:\Users\Administrator\Desktop\data_process.xlsx')


if __name__ == '__main__':
    main()
