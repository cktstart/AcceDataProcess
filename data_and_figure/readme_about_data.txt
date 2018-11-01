# 数据说明：
	# 原始数据是来自jifang:/SRCCData/OriginalTRP/LDSF/20180210/93273/10-6-003_point19的数据，采样率为1024Hz。
	
# --------------------以下是计算结果-----------------------------------------

	# ori_plot_1是原始数据的时域波形图；
	
	# ponit_19_PSD_data.asc是将原始数据在LMS软件上进行PSD计算（默认参数）得到的数据；

	# point19_PSD图片是原始数据在LMS软件计算PSD得到的结果波形；

	# myTest_PSD_OutPxx.txt文件、myTest_PSD_OutFreqs.txt文件和psd_1图片都是第一次进行用python进行PSD计算，delta_f = 1Hz得到的结果。其中，outPxx是psd_1的纵坐标数据，Freqs是psd_1的横坐标数据；

	# 同理，psd_2图片及Pxx_2是delta_f = 0.2 Hz得到的结果；

	# psd_3图片及Pxx_3是delta_f = 0.125 Hz得到的结果；

# ----------以上三个结果都是直接对原始数据进行PSD计算得到的，未进行滤波----------------

	# filted_plot_1是对原始数据进行低通滤波后得到的波形，截止频率为90Hz，（得到的数据放在本地文件中，不在此）；

	# psd_11图片及Pxx_11文件是在上一步滤波后的数据上用python计算PSD得到的结果；



