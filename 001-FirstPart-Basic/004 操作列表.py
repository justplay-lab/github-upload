#coding=gbk
#
### 4.1.1 For循环 : for语句能获得值，则执行print，否则，跳出循环；
#
'''
magicians = ['alice','david','carolina']

for magician in magicians:   #读取第一个值alice赋值给magician
	print(magician.title())  #打印出已经赋值过的magician
'''
#
# 4.1.2 For循环 更多的操作
#
'''
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see ur next trick, " + magician.title() + "\n")
'''
#
# 4.1.3 For循环 结束后执行的一些操作
#
'''
print("Thank you, everyone. That was a great magic show!")
print(magician)  #  For循环结束后，magician保存最后一个元素的值；
'''
#
### 4.3 创建数值列表
#
# 4.3.1 函数range()
#
'''
for value in range(1,5): # 打印数字1~4,数值达到指定值5 后停止
	print(value)
'''
#
# 4.3.2 函数range()创建数字列表;
#
'''
numbers = list(range(1,6)) # 使用函数list()将range()的结果直接转换为列表
print(numbers)
'''
#
# 		函数range()可以指定步长
#
'''
even_numbers = list(range(2,11,2)) # 求偶数, 从2开始，不断加2，直到>=11;
print(even_numbers)
'''
#
#		求1~10的平方，把他们包含进一个列表中
#
'''
squares = []
for value in range(1,11):
	squares.append(value**2)
#	square = value**2
#	squares.append(square)
	
print(squares)
'''
#
# 4.3.3 对数字列表执行简单的统计计算
#
'''
digits = [1,2,3,4,5,6,7,8,9,0]
min_value = min(digits)
max_value = max(digits)
sum_value = sum(digits)
print(digits)
print("min: " + str(min_value) + " max: " + str(max_value) + " sum: " + str(sum_value))
'''
#
# 4.3.4 列表解析
#
'''
squares = [value**2 for value in range(1,11)]
print(squares)
'''
#
# Hands On
#
# 4-4 一百万
'''
digits = list(range(1,1000001))

for digit in digits:
	print(digit)
'''
# 4-5 计算1~1000000的总和
'''
print(min(digits))
print(max(digits))
print(sum(digits))   # 这个加法太快了
'''
# 4-6 奇数
'''
odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
	print(odd_number)
'''
#
# 4.4 切片 : 以运动队成员列表
#
players = ['charles','martina','maichael','florence','eli']
'''
print(players[0:3])  #到了第四个值后，不显示，且跳出；
print(players[:4])   #不指定第一个索引，即从头开始；
print(players[2:])   #不指定第二个索引，即直到最后；
print(players[-2:])  #这里负数功能也适用，这里即倒数第二个开始到最后；
'''
#
# 4.4.2 遍历切片
#
'''
print("Here are the first three players on my team:")
for player in players[:3]:   
	print(player)
'''
#
# 4.4.3 复制列表
#
'''
my_foods = ['pizza','falafel','carrot cake']
'''
#
# 这里两个参数省略，即从头到尾复制整个列表；即my_foods的副本存储到了friend_foods
# 注意：此后，这两个列表是两个完全独立的列表了；
#
'''
friend_foods = my_foods[:] 
print("my favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
'''
#
# 语法注意： friend_foods = my_foods  
# =>即让python将新变量friend_foods关联到包含在my_foods的列表，它们指向同一个列表
#
#
# 4.5 元组 : Python将不能修改的值成为不可变的，其列表成为 元组
#           列表符号[],而元组符号为()
#
# 
# 4.5.1 定义元组
#
dimensions = (200,50)
print(dimensions[0])     # 使用的语法与访问列表语法相同
print(dimensions[1])
# dimensions[0] = 300   =>报 不能给元组赋值错误
#
# 4.6 设置代码格式
#
