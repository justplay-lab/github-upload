#coding=gbk
#
# 7.1 ����input()�Ĺ���ԭ�� : �ó�����ͣ���ȴ��û�����һЩ > �ı� <��
#
# parrot
'''
message = input("Tell me sth, and i will repeat it back to you:")
print(message)
'''
#
# 7.1.1 ��д�����ĳ���
#
# greeter1
'''
name = input("Please enter your name: ")
print("Hello, " + name + "!")
'''
# greeter2
'''
prompt = 'If you tell us who you are, we can personalize the message you see.'
prompt += "\nWhat is your first name? "
name = input(prompt)

print("\nHello, " + name + '!')
'''
#
# 7.1.2 ʹ��int()����ȡ>��ֵ<����
#
'''
age = input("How old are you?")
print(int(age) + 1)
'''
#
# 7.1.3 ��ģ�������% �����������������������
#
# even or odd
'''
number = input("Enter a num, and I'll tell u if it's ever or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd")
'''
#
# 7.2 while ѭ������ : ѭ�����ϵ����У�ֱ��ָ��������������λ�á�
#
# counting
'''
cur_number = 1
while cur_number <=5:
    print(cur_number)
    cur_number += 1

print("after out of while,cur_number's value is : " + str(cur_number))
'''
#
# 7.2.2 ���û�ѡ���ʱ�Ƴ�
#
# parrot
'''
prompt = "\nTell me sth, and i'll repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
'''
'''
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)
'''
#
# 7.2.3 ʹ�ñ�־ �� ����һ�������������ж����������Ƿ��ڻ״̬��
#  
'''               �䵱����Ľ�ͨ�źŵơ�
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
'''
#
# 7.2.4 ʹ��break�˳�ѭ�� �� �����˳�����������ѭ�������µĴ���
#                         ���κ�Pthonѭ���ж���ʹ��break��䡣
# cities
'''
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
'''
#
# 7.2.5 ��ѭ����ʹ��continue�����ص�ѭ����ͷ���������������Խ�������Ƿ����ִ��ѭ��
#
# counting
'''
cur_num = 0
while cur_num < 10:
    cur_num += 1
    if cur_num % 2 == 0:   # ��ֻ��ӡ������
        continue           # ����ѭ�������µĴ��룬���ص�ѭ���Ŀ�ͷ
    
    print(cur_num)
'''
#
# 7.2.6 ��������ѭ�� �� ���������������ѭ�����ɰ�Ctrl + C����ر��ն˴��ڣ�
# 
#
# 7.3 ʹ��whileѭ���������б���ֵ�
# 
# confrimed_users
'''
# ���ȣ�����һ������֤�û��б� �� һ�����ڴ洢����֤�û��Ŀ��б�
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
# ��֤ÿ���û���ֱ��û��δ��֤�û�Ϊֹ����ÿ��������֤���б��ƶ�������֤�û��б���
while unconfirmed_users:
    cur_user = unconfirmed_users.pop()
    
    print("Verifying users: " + cur_user.title())
    confirmed_users.append(cur_user)
# ��ʾ��������֤���û�
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''
#
# 7.3.2 ɾ�������ض�ֵ�������б�Ԫ��
#
# pets
'''
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)
'''
#
# 7.3.3 ʹ���û�����������ֵ�
#
# mountain_poll
responses = {}
# ����һ����־��ָ�������Ƿ����
polling_active = True

while polling_active:
    # ��ʾ���뱻�����ߵ����ֺͻش�
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    
    # �����洢���ֵ���
    responses[name] = response
    
    # �����Ƿ�����Ҫ�������
    repeat = input("Would you like to let another person respond? (yes or no)")
    if repeat == 'no':
        polling_active = False
        
# �����������ʾ���
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
