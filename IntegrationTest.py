

# 将读取的数据标准化
def format_data(row):
	data = row.strip()
	# print(data)
	data = '{:.10f}'.format(float(data))   # 注意精度不够
	data = float(data)
	# print(data)
	return data



delta_x=1

with open(r'C:\Users\user\Desktop\ZZ\data_and_figure\myTest_PSD_OutPxx.txt','r') as file:
	# 测试每行多少字节
	# row = file.readline()   
	# print(file.tell())
	row_len = 26   # 一行26字节

	area=0   # 数组积分，即面积
	# 要积分的区间
	start = 71
	end = 90

	file.seek(start*26,0)   # 直接测试最后一阶段的数据
	for k in range(start,end):
		row1=file.readline()
		# print(row1)
		data1=format_data(row1)
		row2=file.readline()
		data2=format_data(row2)
		# print(data1,"---",data2)
		area+=(data2+data1)/2*delta_x
		# file.seek(-1,1)    # 这个地方不知道为啥不行，暂时搁置！！！
		pos=file.tell()
		file.seek(pos-row_len, 0)   # 滚动向前
		# print(area)

	# area = '{:.10f}'.format(float(area))
	print(area)     # 未滤波，python计算psd后, 1.39515e-06，和LMS结果一样。完美

