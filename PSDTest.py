
import numpy as np

import matplotlib.pyplot as plt 



# ---------------取原始数据--------------

file_name = r'C:\Users\user\Desktop\汽车平顺性试验方法\加速度数据\10-6-003_Point19_filted_data.txt'

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


# -------------------原始波形图（时域）-------------

# plt.figure(figsize=(20,8))
# 画出原始数据 x--y
# plt.subplot(211)
# plt.plot(ylst,"k--")
# plt.xlabel("Time in s")
# plt.ylabel("g")
# # 这里中文标题显示乱码
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# plt.title(u"加速度时域波形图")
# plt.show()
# plt.savefig('./ori_plot_2.png')

# ---------------------计算PSD-------------------


fs = 1024  # 采样频率
# n = range(0,1,step=1/fs)   # 这种不行，因为range方法没有step参数
# n = np.arange(0, 1, step=1/fs)  # 这个应该可以，但是会使得hanning窗出现模糊不清错误，待解决!!
# n = 1024

noverlap = 50   # 50%的重叠
# nfft = 1024  # delta_f = 1/T = fs/nfft = 1 Hz
# nfft = 5120  # delta_f = 1/T = fs/nfft = 0.2 Hz
nfft = 8192  # delta_f = 1/T = fs/nfft = 0.125Hz
window = np.hanning(nfft)    # 加窗


plt.figure(figsize=(20,8))
# plt.subplot(212)
[Pxx, freqs, line] = plt.psd(ylst, Fs=fs, window=window, noverlap=noverlap, NFFT=nfft, return_line=True)

print(type(Pxx))  # <class 'numpy.ndarray'>
print(type(freqs))

# 将PSD结果数据存储，查看是否和LMS软件输出的一致

# np.savez('./myTest_PSD_OutData.txt', Pxx, freqs)  #　.ｎpz格式的文件，不方便

# 未滤波  1Hz
# np.savetxt('./data_and_figure/myTest_PSD_OutPxx_2.txt', Pxx)   # 512个数据点，和LMS产生的PSD数据点一样，但值不同，明天来调试
# np.savetxt('./data_and_figure/myTest_PSD_OutFreqs_2.txt', freqs)

# 未滤波  0.2Hz
# np.savetxt('./data_and_figure/myTest_PSD_OutPxx_3.txt', Pxx)   # 4096个数据点，
# np.savetxt('./data_and_figure/myTest_PSD_OutFreqs_3.txt', freqs)

# 滤波后 0.125Hz
# np.savetxt('./data_and_figure/myTest_PSD_OutPxx_11.txt', Pxx)   # 4096个数据点，
# np.savetxt('./data_and_figure/myTest_PSD_OutFreqs_11.txt', freqs)



# -----------结果-----------------

plt.xlabel("Frequency / (Hz)")
plt.ylabel("（m^2）/s^3")
# plt.show()

# plt.title(u"加速度PSD波形图(1Hz)")
# plt.savefig('./data_and_figure/psd_1.png')

# plt.title(u"加速度PSD波形图(0.2Hz)")
# plt.savefig('./data_and_figure/psd_2.png')

# plt.title(u"加速度PSD波形图(0.125Hz)")
# plt.savefig('./data_and_figure/psd_3.png')


plt.title(u"加速度PSD波形图(滤波后_0.125Hz)")
# plt.savefig('./data_and_figure/psd_11.png')


# plt.show()


