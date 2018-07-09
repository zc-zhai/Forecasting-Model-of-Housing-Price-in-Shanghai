import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv
import seaborn as sns
import numpy as np
import seaborn as sns

# data = randn(80)
# plt.hist(data, alpha=0.3, color='#ffffff')
# sns.rugplot(data)

df = read_csv("test2.csv", encoding="GBK",index_col='index')
df[:2]
clean_df = df[df['S'] < 300]

sub_df = pd.DataFrame(data=clean_df, columns=['Price', 'S'])

sns.pointplot("S", "Price", data=clean_df,alpha=0.8)

# plt.ylabel('Price', fontsize=12)
#
# plt.xlabel('S', fontsize=12)
#
# plt.xticks(rotation='vertical')
plt.show()

# with sns.axes_style("white"):
#     sns.jointplot('Price', 'S', data=sub_df, kind="hex")
#     plt.ylim([0, 600])
#     plt.xlim([0, 200])
# tips = sns.load_dataset("tips")
# g = sns.jointplot(x="S", y="Price", data=clean_df)
# g2 = sns.jointplot(x="S", y="Price", data=clean_df, kind="scatter")
# g3 = sns.jointplot("S", "Price", data=clean_df, kind="reg")
# g7 = (sns.jointplot("S", "Price", data=clean_df, color="k")
#       .plot_joint(sns.kdeplot, zorder=0, n_levels=6))
# sns.kdeplot(data.X, data.Y, shade=True, bw="silverman", gridsize=50, clip=(-11, 11))
# plt.show()