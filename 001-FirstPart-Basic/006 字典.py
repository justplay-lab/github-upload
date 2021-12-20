#coding=gbk
#
# 6.1 一个简单的字典
#
'''
alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])
'''
#
# 6.2 使用字典 ： 字典是一系列 键-值 对。每个键都与一个值相关联，
#               你可以使用键来访问与之相关联的值。
#               与键相关联的值可以是数字、字符串、列表乃至字典。
#               事实上，可将任何Python对象用作字典中的值。 花括号{} 表示
#
# 6.2.2 添加 键-值 对 (动态结构)
#
#       也可以重新创建一个空字典: alien_0 = {},再添加 键-值 对 且无关顺序
'''
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
'''
#
# 6.2.4 修改字典中的值
#
'''
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0['speed'] = 'medium'  # 给外星人添加 速度 键值对
print(alien_0)

print("Original x_position: " +  str(alien_0["x_position"]))
'''
#
# 向右移动外星人，据外星人当前速度决定将其移动多远
#
'''
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))
'''
#
# 6.2.5 删除 键值对： 可使用del语句彻底删除
#
'''
del alien_0['points']
print(alien_0)
'''
#
# 6.2.6 由类似对象组成的字典
#
'''
favorite_languages = {
    'jen':  'python',
    'sarah':  'c',
    'edward':  'ruby',
    'phil':  'python',
    'adam':  'python',
    }

print("Sarah's favorite language is " +   # 长语句分拆后 拼接
    favorite_languages['sarah'].title() + ".")
'''
#
# 6.3 遍历词典：可遍历所有键值对/键/值
#
'''
user_0 = {
    'username': 'efermi',
    'first':    'enrico',
    'last': 'fermi',
    }
'''
#
# 遍历键值
#
'''
for key, value in user_0.items():  # 用简单的变量名k,v替换key,value完全可行
    print('\nKey: ' + key)
    print('Value: ' + value)
'''
#
# 遍历键
#
'''
friends = ['phil','sarah']

for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + 
            ", I see ur favorite language is " +
            favorite_languages[name].title() + ".")

if 'erin' not in favorite_languages.keys(): # 返回一个包含所有key的列表并验证
    print('Erin, please take our poll!')
'''
#
# 6.3.3 按顺序遍历字典中的所有键
#
'''
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
'''
#
# 6.3.4 遍历字典中的所有值
#
'''
for language in favorite_languages.values(): #返回所有值的列表
    print(language.title())

for language in set(favorite_languages.values()): # set集合的使用剔除重复项
    print(language.title())
'''
#
# 6.4 嵌套：在列表中嵌套字典/在字典中嵌套列表/在字典中嵌套字典
#
'''
#
# 6.4.1 字典列表 ： 成群结队的外星人
#
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green','points': 5,'speed': 'slow'}
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print('...')
# 显示创建了多少个外星人
print('Total number of aliens: ' +str(len(aliens)))
# 修改前三个外星人的属性
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
'''
#
# 6.4.2 在字典中存储列表
#
'''
favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c','c++'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell'],
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
'''
#
# 6.4.3 在字典中存储字典
#
users = { 
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location':'paris',
        },
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
