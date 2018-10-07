#Basic_List_Tuple
##使用list和tuple
colleagues=['Allen','Tony','Jack','Mary']
print(colleagues)
print(len(colleagues))
#第一个
print(colleagues[0])
#倒数第一个
print(colleagues[-1])
#插入元素，默认追加到末尾
colleagues.append('hellen')
print(colleagues)
#插入指定位置
colleagues.insert(1,'Ben')
print(colleagues)
#删除末尾元素，Pop()方法
colleagues.pop()
print(colleagues)
#删除指定位置的元素，用pop(i)指定
colleagues.pop(0)
print(colleagues)
#替换某个元素，直接赋值修改
colleagues[1]='Sarah'
print(colleagues)
#list里边的元素数据类型不一定一致
li=['apple',123,True]
print(li)
#list元素也可以是另一个list
li=['apple',2,[3,'a'],1]
print(li)
p=[3,'a']
#要在li中取到'a'值，把li当做二维数组
print(p[1])
print(li[2][1])
#获取长度
print(len(li))

#tuple（元组）:有序列表，与list类似，但初始化后就不可更改的。
#陷阱：定义时其元素就必须确定下来
t=(1,2)
print(t)
#定义空tuple
t=()
#定义只有1个元素的tuple
t=(2,) #由于如果写成t=(2)，其中的括号及其容易被解读为数学符号，从而定义的只是数字2
#指向不变，但看似修改了的tuple:
#其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list
t=('a','b',['A','B'])
t[2][0]='x'
t[2][1]='y'
print(t)

#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
#打印Apple
print(L[0][0])
#打印Python
print(L[1][1])
#打印Lisa
print(L[2][2])

