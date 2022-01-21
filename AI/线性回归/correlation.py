# 这个文件的目的在于显示如何使用pandas去得到我们的相关性
import pandas as pd
import seaborn as sns

data = pd.read_csv("./Mult_regression/Fish.csv")
# In the method you can use the person, kendall, spearman or the one define by yourself
data = data.corr(method='pearson')

fig_name = './heatmap.png'
fig = sns.heatmap(data, annot=True, cmap='YlGnBu')
fig1 = fig.get_figure()
fig1.savefig(fig_name, dpi=400)
