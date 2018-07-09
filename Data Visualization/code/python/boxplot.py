import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import seaborn as sns

with open("test.csv", "r", encoding="GBK") as f:
    reader = csv.reader(f)
    column = [row[0] for row in reader]

def liston(m,n):
    sel1 = column[m:n]
    print(type(sel1))
    print(sel1)
    sel2 = [float(i) for i in sel1] #定义一个截取列表以及修改格式的函数
    return sel2
    # print(len(sel2))
    # sel2.append(0)
    # sel2.append(10000)
    # print(len(sel2))
    # data = pd.DataFrame({"bs": sel2
    #                      })
    # "Wasserstein":list3
    # "KL-divergence":list4}
    # data.boxplot() 
    # plt.ylabel("Price")
    # plt.xlabel("Address")  # 设置横纵坐标的标题
    # plt.show()
    # sel5 = sel1
    # print(len(sel1))
    # n = 0
    # for i in sel1:
    #     sel5[n] = float(i)
    #     n += 1
    # print(sel5)
    # print(type(sel5))
    # sel2 = str(sel1).replace("'", "")
    # print(sel2)
    # print(sel1[4])
    # print(int(sel1[4])+1)
    # sel3 = int(sel2)
    # print(sel3)
    # print(type(sel3))

    # for row in reader:
    #     print(row)

bs=liston(0,300)
cn=liston(2996,3296)
fx=liston(5997,6297)
hk=liston(7171,7471)
hp=liston(10032,10332)
ja=liston(12233,12533)
js=liston(13544,13844)
cm=liston(13650,13950)
shzb=liston(13697,13997)
jd=liston(13728,14028)
qf=liston(16550,16850)
sj=liston(19100,19400)
yp=liston(21741,22041)
zb=liston(24741,25041)
mh=liston(27504,27804)
pdq=liston(30506,30806)
pt=liston(33418,33718)
xh=liston(36420,36720)

data = pd.DataFrame({
                     "bs": bs,
                     "cn": cn,
                     "fx": fx,
                     "hk": hk,
                     "hp": hp,
                     "ja": ja,
                     "js": js,
                     "cm": cm,
                     "shzb": shzb,
                     "jd": jd,
                     "qf": qf,
                     "sj": sj,
                     "yp": yp,
                     "zb": zb,
                     "mh": mh,
                     "pdq": pdq,
                     "pt": pt,
                     "xh": xh
                     })
                     #各个区的list作为输入

# sns.set(color="pastel", widths=.5)
# sns.set_style("darkgrid")
data.boxplot()  #绘制箱线图
# set('LineWidth',2);
plt.ylabel("Price:w") #添加y轴label
plt.xlabel("Address:district") #添加x轴的label
plt.show()