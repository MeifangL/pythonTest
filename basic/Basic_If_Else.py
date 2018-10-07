#Basic_If_Else
#注意不要少写了冒号:
age = 20
#age = input ('age:') #此处默认输入的是str
age = int(age) #漏掉类型转换会报错，str不能直接和int比较
if age >= 18:
	print('your age is ',age)
	print('adult')
elif age >=12: #elif是else if的缩写
	print('your age is ',age)
	print('teenager')
else:
	print('kid')


#练习
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
weight = 80.5
height = 1.75
bmi = weight/(1.75*1.75) #默认除出来就是带小数点的
#print('%.1f' % bmi)
print(bmi)
if(bmi<18.5):
	print('过轻')
elif (bmi<25):
	print ('正常')
elif (bmi<28):
	print('过重')
elif (bmi<32):
	print('肥胖')
else:
	print('严重肥胖')
