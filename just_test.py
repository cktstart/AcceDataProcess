

# 将读取的数据标准化
def format_data(row):
	data = row.strip()
	# print(data)
	data = '{:.8f}'.format(float(data))   # 开始去6位小数，结果是0，因为精度不够
	data = float(data)
	# print(data)
	return data



delta_x=1
row_num=90
with open(r'C:\Users\user\Desktop\汽车平顺性试验方法\加速度数据\10-6-003_point9_psd.asc','r') as file:

	# 测试每行多少字节
	# row = file.readline()   
	# print(file.tell())
	row_len = 19   # 一行19字节

	file.seek(71*19,0)   # 直接测试最后一阶段的数据
	area=0
	for k in range(71,90):
		row1=file.readline()
		# print(row1)
		data1=format_data(row1)
		row2=file.readline()
		data2=format_data(row2)
		# print(data1,"---",data2)
		area+=(data2+data1)/2*delta_x
		# file.seek(-1,1)    # 这个地方不知道为啥不行，暂时搁置！！！
		pos=file.tell()
		file.seek(pos-19,0)
		# print(area)

	print(area)   # 未滤波，LMS计算PSD后，1.39e-06















