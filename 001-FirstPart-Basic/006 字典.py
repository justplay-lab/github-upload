#coding=gbk
#
# 6.1 һ���򵥵��ֵ�
#
'''
alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])
'''
#
# 6.2 ʹ���ֵ� �� �ֵ���һϵ�� ��-ֵ �ԡ�ÿ��������һ��ֵ�������
#               �����ʹ�ü���������֮�������ֵ��
#               ����������ֵ���������֡��ַ������б������ֵ䡣
#               ��ʵ�ϣ��ɽ��κ�Python���������ֵ��е�ֵ�� ������{} ��ʾ
#
# 6.2.2 ��� ��-ֵ �� (��̬�ṹ)
#
#       Ҳ�������´���һ�����ֵ�: alien_0 = {},����� ��-ֵ �� ���޹�˳��
'''
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
'''
#
# 6.2.4 �޸��ֵ��е�ֵ
#
'''
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0['speed'] = 'medium'  # ����������� �ٶ� ��ֵ��
print(alien_0)

print("Original x_position: " +  str(alien_0["x_position"]))
'''
#
# �����ƶ������ˣ��������˵�ǰ�ٶȾ��������ƶ���Զ
#
'''
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    
# ��λ�õ�����λ�ü�������
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))
'''
#
# 6.2.5 ɾ�� ��ֵ�ԣ� ��ʹ��del��䳹��ɾ��
#
'''
del alien_0['points']
print(alien_0)
'''
#
# 6.2.6 �����ƶ�����ɵ��ֵ�
#
'''
favorite_languages = {
    'jen':  'python',
    'sarah':  'c',
    'edward':  'ruby',
    'phil':  'python',
    'adam':  'python',
    }

print("Sarah's favorite language is " +   # �����ֲ�� ƴ��
    favorite_languages['sarah'].title() + ".")
'''
#
# 6.3 �����ʵ䣺�ɱ������м�ֵ��/��/ֵ
#
'''
user_0 = {
    'username': 'efermi',
    'first':    'enrico',
    'last': 'fermi',
    }
'''
#
# ������ֵ
#
'''
for key, value in user_0.items():  # �ü򵥵ı�����k,v�滻key,value��ȫ����
    print('\nKey: ' + key)
    print('Value: ' + value)
'''
#
# ������
#
'''
friends = ['phil','sarah']

for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + 
            ", I see ur favorite language is " +
            favorite_languages[name].title() + ".")

if 'erin' not in favorite_languages.keys(): # ����һ����������key���б���֤
    print('Erin, please take our poll!')
'''
#
# 6.3.3 ��˳������ֵ��е����м�
#
'''
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
'''
#
# 6.3.4 �����ֵ��е�����ֵ
#
'''
for language in favorite_languages.values(): #��������ֵ���б�
    print(language.title())

for language in set(favorite_languages.values()): # set���ϵ�ʹ���޳��ظ���
    print(language.title())
'''
#
# 6.4 Ƕ�ף����б���Ƕ���ֵ�/���ֵ���Ƕ���б�/���ֵ���Ƕ���ֵ�
#
'''
#
# 6.4.1 �ֵ��б� �� ��Ⱥ��ӵ�������
#
# ����һ�����ڴ洢�����˵Ŀ��б�
aliens = []
# ����30����ɫ��������
for alien_number in range(30):
    new_alien = {'color': 'green','points': 5,'speed': 'slow'}
    aliens.append(new_alien)
# ��ʾǰ���������
for alien in aliens[:5]:
    print(alien)
print('...')
# ��ʾ�����˶��ٸ�������
print('Total number of aliens: ' +str(len(aliens)))
# �޸�ǰ���������˵�����
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
# ��ʾǰ5��������
for alien in aliens[:5]:
    print(alien)
print("...")
'''
#
# 6.4.2 ���ֵ��д洢�б�
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
# 6.4.3 ���ֵ��д洢�ֵ�
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
