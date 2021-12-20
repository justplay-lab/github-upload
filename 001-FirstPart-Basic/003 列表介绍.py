#coding=gbk
'''
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0].title())  #start from ZERO
print(bicycles[-1].title()) #!!! -1 means the last one!!!!

names = ['david','peter','Paul','Michael','Adam']
print(names[0])
...

print(names[0].title() + ' welcome learn Python Together!')
...

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# APPEND
motorcycles.append('ducati')  # add from the end
print(motorcycles)

# INSERT
# [0]-end all elements move right ONE place,put 'ducati' in [0],
motorcycles.insert(0,'ducati') 
print(motorcycles)

# DEL  要知道元素在列表中的位置，删除后无法再访问.
del motorcycles[0]
print(motorcycles)

# POP() 相当于弹出栈顶元素，可接着使用它
# 亦可以弹出指定 元素;弹出的元素 就 不再在 列表中了
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

first_owned = motorcycles.pop(1)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")
print(motorcycles)

# REMOVE 删除 指定 值的元素, 该值也可以继续使用，因为你已经知道它的值了，呵呵
motorcycles.remove('ducati')
print(motorcycles)
'''
'''
# 3-4 guest list
guests = ['adam','charlie','david','ominic','peter']
print("Guests' list as below:")
print(guests)
# 3-5 modify the list
print('David will not attend !!')
print('will replace David with beauty')
print('Now the list as below')
guests.remove('david')
guests.append('beauty')
print(guests)
# 3-6 add guest to the list
print('Found A Bigger Table, Refresh the list')
guests.insert(0,'anny')
guests.insert(3,'newton')
guests.append('monica')
print(guests)
# 3-7 reduce the list
print('Can only dinner with 2 friend!!')
del_guest1 = guests.pop()
del_guest2 = guests.pop()
del_guest3 = guests.pop()
del_guest4 = guests.pop()
del_guest5 = guests.pop()
del_guest6 = guests.pop()
print('Sorry, my friend ' + del_guest1 + " and " + del_guest2)
print('Sorry, my friend ' + del_guest3 + " and  " + del_guest4)
print('Sorry, my friend ' + del_guest5 + " and  " + del_guest6)
print(guests)
print("OOPS, all not available!!")
del guests[0]
print(guests)
del guests[0]
print(guests)
'''

# 3.3.1 SORT() 对列表进行永久性排序
cars = ['bmw','audi','toyota','subaru']
print('Here is the original list:')
print(cars)
'''
cars.sort()
print(cars)

# SORT   中reverse反序排列,也是永久性的
cars.sort(reverse=True)
print(cars)

# SORTED() 对列表进行临时排序 也适用reverse属性
print('\nHere is the sorted list:')
print(sorted(cars))
print("\nHere is the original list again!")
print(cars)

# 3.3.3 倒着打印列表 
# REVERSE() 反转列表元素的排列顺序；永久性改变；要想恢复再调用一次即可
cars.reverse()
print(cars)
'''
# 3.3.4 确定列表长度
# LEN() 获悉列表长度
print(len(cars))
