import os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir("D:\\b站流量分析（python期末项目）\\b站流量分析\\data_save")#设置成存放数据文件夹路径
data = pd.read_csv("description.csv", encoding = 'utf-8')
plt.rcParams['font.sans-serif'] = ['SimHei']   #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False
df = pd.DataFrame(data)
X = list(df.iloc[:, 2])
print(X)
Y = list(df.iloc[:, 5])
print(Y)
plt.bar(X, Y, color='g')
plt.title("评论性别获赞统计")
plt.xlabel("用户性别")
plt.ylabel("点赞数")
plt.show()