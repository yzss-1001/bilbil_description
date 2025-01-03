import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import os
import pandas as pd
os.chdir("D:\\b站流量分析（python期末项目）\\b站流量分析\\data_save")#设置成存放数据文件夹路径
date = pd.read_csv("description.csv", encoding = 'utf-8')#读取数据
plt.rcParams['font.sans-serif'] = ['SimHei']   #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False    # 解决中文显示问题
date = date.set_index('性别')
result = date[['点赞']].groupby(date.index).sum()
# print(result)
plt.pie(result['点赞'], labels=result.index, autopct='%3.1f%%')
plt.title('评论获赞与性别比例')#标题
plt.show()




