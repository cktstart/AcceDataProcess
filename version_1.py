

import numpy as pd
import time
import pandas as pd
from pandas import Series,SparseDataFrame
import matplotlib.pyplot as plt 

# # 滤波模块
# def myFilter()



# # psd模块
# def myPSD()



# # 数值积分模块
# def myIntegration()


# 画图
def myPlot(x,y):
	'''
		@作用：画出原始数据x-y波形图
		@x,y: 同长度的一维列表
	'''

	plt.figure(figsize=(20,8))

	# 画出原始数据 x--y
	plt.plot(x,y,"k--")
	plt.xlabel("Time in s")
	plt.ylabel("g")
	# 这里中文标题显示乱码
	plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
	plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
	plt.title(u"加速度时域波形图")

	# time_start = time.time()
	plt.show()   # 3 秒
	# plt.savefig('./time_plot_1.png')
	# time_end = time.time()
	# print("savefig take time : {0:.3f}".format(time_end - time_start))



# 读文件开始
def myInput(file_name):
	df = pd.read_excel(file_name,usecols=[3,4]) # 读取指定列（第4,5列）
	x = list(df.iloc[0:,0])  # 剔除标题行，取横坐标-时间
	y = list(df.iloc[0:,1])  # 剔除标题行，取纵坐标-加速度
	myPlot(x,y)





# 全局变量
file_name = r'C:\Users\user\Desktop\汽车平顺性试验方法\加速度数据\123458#7Waveform_0.125s.XLS'

myInput(file_name)



