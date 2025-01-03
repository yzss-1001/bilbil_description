import os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir("D:\\b站流量分析（python期末项目）\\b站流量分析\\data_save")#设置成存放数据文件夹路径
date = pd.read_csv("description.csv", encoding = 'utf-8')
plt.rcParams['font.sans-serif'] = ['SimHei']   #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False
date = date.set_index('经验')
result = date[['点赞']].groupby(date.index)
result1 = date[['点赞']].groupby(date.index).sum()
df = pd.DataFrame(result)
df1 = pd.DataFrame(result1)
X = list(df.iloc[:,0])
X_str = []
for i in X:
    i=str(i)
    X_str.append(i)
print(X_str)
Y = list(df1.iloc[:,0])
print(Y)
plt.bar(X_str, Y, color='g')
plt.title("不同经验的获赞数")
plt.xlabel("用户经验")
plt.ylabel("点赞数")
plt.show()