# -*- coding: utf-8 -*-

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd


# ---------------取原始数据--------------

# ----这是已经进行PSD以后的数据，不对
# file_name = r'C:\Users\user\Desktop\汽车平顺性试验方法\加速度数据\123458#7Waveform_0.125s.XLS'
# df = pd.read_excel(file_name,usecols=[3,4]) # 读取指定列（第4,5列）
# # x = df.iloc[0:,0] # 剔除标题行，取横坐标-时间
# y = df.iloc[0:,1]  # 剔除标题行，取纵坐标-加速度
# ys = y.values
# # print(y.values)   # [-0.000658 -0.000686 -0.000574 ... -0.000447 -0.000477 -0.000522]
# # print(type(y.values))  # <class 'numpy.ndarray'>
# ylst = list(ys)
# # print(ys)  # done


# ----这才是原始数据，还未进行PSD计算
file_name = r'C:\Users\user\Desktop\汽车平顺性试验方法\加速度数据\10-6-003_Point19_origin_data.asc'

# 将读取的数据标准化
def format_data(row):
	data = row.strip()
	# print(data)
	data = '{:.8f}'.format(float(data))   # 6位小数的精度不够
	data = float(data)
	# print(data)
	return data


with open(file_name,'r') as file:
	# data = []
	ylst = list(map(format_data, file.readlines()))   #  time-20s
	# print(type(data[0]))  # <class 'float'>
	# print(data)



# -------------------原始波形图-------------

plt.figure(figsize=(20,8))
# 画出原始数据 x--y
# plt.subplot(211)
# plt.plot(ylst,"k--")
# plt.xlabel("Time in s")
# plt.ylabel("g")
# # 这里中文标题显示乱码
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# plt.title(u"加速度时域波形图")
# # plt.show()
# plt.savefig('./data_and_figure/ori_plot_2.png')


# -------------------低通滤波--------------

# 原始采用频率为1024Hz，截止频率取90Hz，则wn = 2*90/1024约为0.088，滤波器阶词设置为8
filter_order = 8
cut_freq = 90
sample_freq = 1024
wn = float('{:.4f}'.format(2*cut_freq/sample_freq))
# print(wn)

b,a = signal.butter(filter_order, wn, 'lowpass')
filted_data = list(signal.filtfilt(b, a, ylst))

# 存储滤波后数据，供PSD计算
np.savetxt('./data_and_figure/filted_data_1.txt', filted_data)


# -------------------滤波后波形图-------------

# plt.subplot(212)
# 画出滤波后数据 x--y
plt.plot(filted_data,"k--")
plt.xlabel("Time in s")
plt.ylabel("g")
plt.title(u"加速度时域波形图(90Hz滤波后)")
# plt.show()
plt.savefig('./data_and_figure/filted_plot_1.png')



