#Basic_Variable_String
##布尔变量
print(3>2)
#bool运算，and,or,not
print(5>3 and 3>1)
print(True and False)
print(True or False)
print(False or False)
print(not 1>2)
#if else，逻辑判断
age=20
if age>=18:
	print('adult')
else:
	print('teenager')
#变量定义，在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
#这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，
#如果赋值的时候类型不匹配，就会报错，例如Java。和静态语言相比，动态语言更灵活
a=100
print('init a: ',a)
a='Cat'
print('now a: ',a)

#赋值语句'='
a = 'ABC'
b = a
a = 'XYZ'
print(b)

#常量：在Python中，通常用全部大写的变量名表示常量：PI，但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，
#所以，用全部大写的变量名表示常量只是一个习惯上的用法
PI=3.14159

# 除法为什么也是精确的：在Python中，有两种除法，一种除法是/，其计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
print(10/2)
print(10/3)
#还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
print(10//3)
#余数运算：%
print(10%3)
#练习
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,"\n",f,"\n",s1,"\n",s2,"\n",s3,"\n",s4)

#字符编码，ASCII，Unicode，UTF-8
#计算字符串长度：len('abc')
print(len('AB'))

#由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
#当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#解释器：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
print('中文测试正常')

#占位符:%d,%f,%s,%x
print('Hi %s, your number is %d' %('mef',1))
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)


#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' %(24,'女'))
#当%本身为普通字符时，需转义，用%%表示%
print('增长率： %d %%' % 7)

#练习小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

# -*- coding: utf-8 -*-
s1=72
s2=85
rate=(s2-s1)/s1
print('%.1f %%' %rate)
