#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#输入输出
#输出
print("hello world!")
print(3+4)
#输入
#name = input('Input your name: ')
#print('Hello,', name)

#转义，用\表示，Python还允许用r''表示''内部的字符串默认不转义
print("I'm \"fine\"")
print(r'\\')

#换行，可以用\n或者…
print(1,"\n")
print(2,"\n")
#用'''内容'''来表示多行，方便阅读
print('''line1
line2
line3''')
#在前面加上r使用
print(r'''hello,\n
world''')

#注释
#多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起
#
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''

"""
这是多行注释，用三个双引号
双引号
双引号
"""