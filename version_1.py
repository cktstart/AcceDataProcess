

<<<<<<< HEAD

# import time
import xlrd
import pandas as pd
import numpy as np
from scipy import signal
from pandas import Series,SparseDataFrame
import matplotlib.pyplot as plt 



# 将读取的数据标准化
def format_data(row):
	data = row.strip()
	# print(data)
	data = '{:.10f}'.format(float(data))   # 注意精度不够
	data = float(data)
	# print(data)
	return data


# # 滤波模块
def myFilter(ylst):
	filter_order = 8
	cut_freq = 90
	sample_freq = 1024
	wn = float('{:.4f}'.format(2*cut_freq/sample_freq))
	# print(wn)

	b,a = signal.butter(filter_order, wn, 'lowpass')
	filted_data = list(signal.filtfilt(b, a, ylst))
	return filted_data
=======
import numpy as pd
import time
import pandas as pd
from pandas import Series,SparseDataFrame
import matplotlib.pyplot as plt 

# # 滤波模块
# def myFilter()
>>>>>>> e912e6a7b28364871a6048b3dfba01376a32bb78



# # psd模块
<<<<<<< HEAD
def myPSD(yfilted):
	fs = 1024  # 采样频率
	noverlap = 50   # 50%的重叠
	# nfft = 1024  # delta_f = 1/T = fs/nfft = 1 Hz
	# nfft = 5120  # delta_f = 1/T = fs/nfft = 0.2 Hz
	nfft = 8192  # delta_f = 1/T = fs/nfft = 0.125Hz
	window = np.hanning(nfft)    # 加窗


	plt.figure(figsize=(20,8))
	[Pxx, freqs, line] = plt.psd(yfilted, Fs=fs, window=window, noverlap=noverlap, NFFT=nfft, return_line=True)
	plt.title(u"加速度PSD波形图(temp)")
	plt.xlabel("Frequency / (Hz)")
	plt.ylabel("（m^2）/s^3")
	# plt.show()

	plt.savefig('./data_and_figure/temppsd_1.png')
	ypsd = list(Pxx)
	xpsd = list(freqs)

	return xpsd,ypsd



# 读取分段信息
def freqSegment(freq_file):
	df = pd.read_excel(freq_file) # ）
	start_lst = list(df.iloc[0:,0])  # 剔除标题行，取开始-下限频率
	end_lst = list(df.iloc[0:,1])  # 剔除标题行，取结束-上限频率
	return start_lst,end_lst


# # 数值积分模块
def myIntegration(start,end,ypsd):
	row_len = 26
	delta_x = 1    # 梯形的高
	area = 0
	for k in range(start,end):
		# row1=file.readline()
		row1 = ypsd[k]
		# print(row1)
		data1=format_data(str(row1))   # numpy.float64' object has no attribute 'strip'
		# row2=file.readline()

		row2 = ypsd[k+1]
		data2=format_data(str(row2))
		# print(data1,"---",data2)
		area+=(data2+data1)/2*delta_x
		# file.seek(-1,1)    # 这个地方不知道为啥不行，暂时搁置！！！
		# pos=file.tell()
		# file.seek(pos-row_len, 0)   # 滚动向前
		# print(area)
	return area

=======
# def myPSD()



# # 数值积分模块
# def myIntegration()
>>>>>>> e912e6a7b28364871a6048b3dfba01376a32bb78


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



<<<<<<< HEAD
# 读excel文件开始
def myInputExcel(file_name):
	df = pd.read_excel(file_name,usecols=[3,4]) # 读取指定列（第4,5列）
	xlst = list(df.iloc[0:,0])  # 剔除标题行，取横坐标-时间
	ylst = list(df.iloc[0:,1])  # 剔除标题行，取纵坐标-加速度
	# myPlot(xlst,ylst)
	return xlst,ylst
	

# 读txt文件，测试用
def myInputTxt(file_name):
	with open(file_name,'r') as file:
		ylst = []
		data = file.readlines()
		for line in data:
			line = format_data(line)  # 处理为float格式，不然为str格式
			ylst.append(line)
		return ylst

# 全局变量
# file_name = r'C:\Users\user\Desktop\汽车平顺性试验方法\加速度数据\10-6-003_Point19_origin_data.asc'   # 原始数据excel文件
freq_file = r'C:\Users\user\Desktop\汽车平顺性试验方法\13倍频带上下限频率.xlsx'    # 1/3倍频带上下限频率表
# xlst,ylst = myInputExcel(file_name)
# filted_data = myFilter(ylst)
# xpsd,ypsd = myPSD(filted_data)

file_name = r'C:\Users\user\Desktop\汽车平顺性试验方法\加速度数据\10-6-003_Point19_origin_data.asc'   # 原始数据txt文件
ylst = myInputTxt(file_name)
xpsd,ypsd = myPSD(ylst)

# myPlot(xpsd, ypsd)

k = 1   # 系数，在psd结果中取对应倍频分段表的区间，
# start_lst,end_lst = freqSegment(freq_file)

area_all = []  # 用来存储最终的分段积分结果

# for i in start_lst:
# 	# 单段的积分
# 	area = 0
# 	# int 是向下取整，经观察，要加1个才刚好
# 	# start = int(start_lst[i]*k)+1
# 	# end = int(end_lst[i]*k)+1
# 	area = myIntegration(start,end,ypsd)
# 	area_all.append(area)


# 测试，71-90段的最后结果是否约等于，未滤波LMS计算PSD后，1.39e-06
# 单段的积分
area = 0
# int 是向下取整，经观察，要加1个才刚好
start = int(71*k)
end = int(90*k)

area = myIntegration(start,end,ypsd)
area_all.append(area)

print(area_all)
=======
# 读文件开始
def myInput(file_name):
	df = pd.read_excel(file_name,usecols=[3,4]) # 读取指定列（第4,5列）
	x = list(df.iloc[0:,0])  # 剔除标题行，取横坐标-时间
	y = list(df.iloc[0:,1])  # 剔除标题行，取纵坐标-加速度
	myPlot(x,y)





# 全局变量
file_name = r'C:\Users\user\Desktop\汽车平顺性试验方法\加速度数据\123458#7Waveform_0.125s.XLS'

myInput(file_name)
>>>>>>> e912e6a7b28364871a6048b3dfba01376a32bb78



