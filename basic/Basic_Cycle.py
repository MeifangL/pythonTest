#Basic_Cycle
#python的循环有2种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
#另一种是while循环，当条件满足就继续循环
fruits = ['apple','banana','orange']
for x in fruits:
	print (x) 

#计算1-100的和
sum = 0
for i in range(1,101): #1+…+100
	sum+=i
print (sum)

#改用while：计算1-100的和
sum = 0
i = 0 
while i<=100:
	sum+=i
	i+=1
print('while循环结果：',sum)

#练习
#请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart','Lisa','Adam']
for li in L:
	print('Hello,',li)

#break，提前结束循环
n=1
while n<=100:
	if(n>10):
		break
	print(n)
	n=n+1
print('END')

#continue,跳过当前的这次循环，直接开始下一次循环
n=0
while n<10:
	n=n+1
	if(n%2==1):
		continue
	print('偶数：',n)