#coding=gbk
#
# 5.1 ��ʾ��
#
'''
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
'''
#
# 5.2 �������� �� True or False
#   
# car = 'bmw'    =>��ֵ��䣬�ɽ��Ϊ��������car��ֵ����Ϊ��bmw����
# car == 'bmw'   =>�Ƚ���䣬����car��ֵΪ'bmw'��
# car.lower() == 'audi' => ����carԭ����ֵ����ı�
#
# 5.2.3 ����Ƿ����
#
'''
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':  # ��ʱ�����Ƿ񲻵�Ч�ʸ���
    print("Hold the anchovies!")
'''
#
# 5.2.5 ���������
#
# 1.ʹ��and���������
# 2.ʹ��or���������
#
# 5.2.6 ����ض�ֵ�Ƿ�  ���� ���б���
#
'''
requested_toppings = ['mushrooms','onions','pineapple']
requested_topping = 'fish'
if requested_topping in requested_toppings:
    print(requested_topping + " in requested toppings!")
else:
    print(requested_topping + " not in requested toppings! ")
'''
#
# 5.2.6 ����ض�ֵ�Ƿ�  ������ ���б���
#
'''
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ",you can post a response if you wish")
'''
#
# 5.2.7 �������ʽ => �������� �ı����������������� Ϊ True Or False
#                   ����: game_active = True �� can_edit = Flase
#
# 5.3 IF ���ṹ �� if / if-else / if-else-else
#
# 5.3.4 ʹ�ö��elif�����: ��������֪������Ҫ���Ե�������
#
'''
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
    
print("your admission cost is $" + str(price) + ".")
'''
#
# 5.4 ʹ��if��䴦���б�
#
# 5.4.2 ȷ���б��ǿյ�
#
'''
requested_toppings = []

if requested_toppings:  ## �б����ٰ���һ��Ԫ��ʱ����true,Ϊ��ʱ����flase
    for requested_topping in requested_toppings:
        print("adding " + requested_topping)
    print("\nFinished makeing your pizza!")
else:
    print("Are you sure you want a plain pizza?")
'''
#
# 5.4.3 ʹ�ö���б�
#
available_toppings = ['mushrooms','olives','green peppers',
                        'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(" Adding " + requested_topping + ".")
    else:
        print(" Sorry, we don' t have " + requested_topping + ".")

print("\nFinished making your pizza!")
