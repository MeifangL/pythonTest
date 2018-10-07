#Basic_Dict_Set
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d={'Michael':95,'Bob':80,'Allen':89}
print(d['Bob'])

d['Adam']=77
print(d['Adam'])
print('now d: ' ,d)
#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['Adam']=78
print("Adam's score:",d['Adam'])
d['Adam']=79
print("Adam's score:",d['Adam'])
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
if ('Thomas' in d):
	print('Thomas!')
else:
	print("Can't found Thomas!'")
#二是通过dict提供的get()方法，不存在则返回None或指定的值
print(d.get('Thomas'))

print(d.get('Thomas',555))

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d)
#dict内部存放的顺序和key放入的顺序是没有关系的
#dict的key必须是不可变对象。因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了
#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
#要创建一个set，需要提供一个list作为输入集合
s = set([1,2,2,5,5,3]) #set中传入的参数是一个list
print(s) #自动过滤重复的
s.add(4)
print (s)
s.remove(2)
print(s)
#set可以看成数学意义上的无序和无重复元素的集合,可做并集和交集
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1&s2) #{2,3}
print(s1|s2) #{1,2,3,4}
