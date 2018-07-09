import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import seaborn as sns

data = pd.read_csv("test2.csv",encoding="GBK")
sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset(data)
print(iris)

g = sns.pairplot(iris)
plt.show()

# print(data)
# sns.set()                        #使用默认配色
# sns.pairplot(data,row="Price")   #hue 选择分类列
# plt.show()