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

# DEL  Ҫ֪��Ԫ�����б��е�λ�ã�ɾ�����޷��ٷ���.
del motorcycles[0]
print(motorcycles)

# POP() �൱�ڵ���ջ��Ԫ�أ��ɽ���ʹ����
# ����Ե���ָ�� Ԫ��;������Ԫ�� �� ������ �б�����
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

first_owned = motorcycles.pop(1)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")
print(motorcycles)

# REMOVE ɾ�� ָ�� ֵ��Ԫ��, ��ֵҲ���Լ���ʹ�ã���Ϊ���Ѿ�֪������ֵ�ˣ��Ǻ�
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

# 3.3.1 SORT() ���б��������������
cars = ['bmw','audi','toyota','subaru']
print('Here is the original list:')
print(cars)
'''
cars.sort()
print(cars)

# SORT   ��reverse��������,Ҳ�������Ե�
cars.sort(reverse=True)
print(cars)

# SORTED() ���б������ʱ���� Ҳ����reverse����
print('\nHere is the sorted list:')
print(sorted(cars))
print("\nHere is the original list again!")
print(cars)

# 3.3.3 ���Ŵ�ӡ�б� 
# REVERSE() ��ת�б�Ԫ�ص�����˳�������Ըı䣻Ҫ��ָ��ٵ���һ�μ���
cars.reverse()
print(cars)
'''
# 3.3.4 ȷ���б���
# LEN() ��Ϥ�б���
print(len(cars))
