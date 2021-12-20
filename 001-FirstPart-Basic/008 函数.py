#coding=gbk
#
# �����������������ֵĴ���飬������ɾ���Ĺ���
#
# 8.1 ���庯��
#
# greeter
'''
def greet_user():
    """��ʾ�򵥵��ʺ���"""  # �ĵ��ַ�����ע�ͣ����������йس����к������ĵ�
    print("Hello!")

greet_user()
'''
#
# 8.1.1 ����������Ϣ
#
'''
def greet_user(username):   # �β�
    """��ʾ�򵥵��ʺ���"""
    print("Hello, " + username.title() + "!")

greet_user('jessie')        # ʵ��
'''
#
# 8.1.2 ʵ�κ��β� : ����
#
#
# 8.2 ����ʵ��
#
# 8.2.1 λ��ʵ�� �� ʵ�κ��β� ˳��Ҫ��ͬ
#
# pets
'''
def des_pet(animal_type, pet_name):
    """��ʾ�������Ϣ"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ",")

des_pet('hamster', 'harry')
des_pet('dog','willie')
'''
#
# 8.2.2 �ؼ���ʵ�Ρ����������ݸ������� ����-ֵ �ԡ�����˳�����޹ؽ�Ҫ��
#
'''
def des_pet(animal_type, pet_name):
    """��ʾ�������Ϣ"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ",")
# ����ʱ��������Python��ȷ��ָ���˸���ʵ�ζ�Ӧ���βΡ�
des_pet(animal_type = 'hamster', pet_name = 'harry') 
'''
#
# 8.2.3 Ĭ��ֵ����������ÿ���β�ָ�� Ĭ��ֵ
#
'''
def des_pet(pet_name, animal_type = 'dog'):  # Python��Ϊλ��ʵ��
    """��ʾ�������Ϣ"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ",")

des_pet(pet_name = 'willie')
des_pet('fly')
des_pet(animal_type = 'hamster', pet_name = 'harry')
'''
#
# 8.2.4 ��Ч�ĺ������� ��  ����
#
# 8.2.5 ����ʵ�δ���λ�� �� ���� ��ƥ��
#
# 8.3 ����ֵ �� ��ʹ��return���
#
# 8.3.1 ���ؼ�ֵ
#
# formatted_name
'''
def get_formatted_name(first_name, last_name):
    """�������������"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
'''
#
# 8.3.2 ��ʵ�α�ɿ�ѡ��
#
'''
def get_formatted_name(first_name, last_name, middle_name=''):
    """���� ���� �� ����"""
    if middle_name:         # ��ֵ��ΪTrue
        full_name = first_name + ' ' + middle_name + ' ' + last_name 
    else:
        full_name = first_name + ' ' + last_name 
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print( musician)
'''
#
# 8.3.3 �����ֵ�
#
# person
'''
def build_person(first_name, last_name, age=""):
    """����һ���ֵ䣬���а����й�һ���˵���Ϣ"""
    person = {'first': first_name, 'last': last_name} #����ֵ����װ���ֵ䷵��
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age = 27)
print(musician)
'''
#
# 8.3.4 ���ʹ�ú�����whileѭ��
#
'''
def get_formatted_name(first_name, last_name):
    """�������������"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break 
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
        
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
'''
#
# 8.4 �����б�������ʹ�ú�������ߴ����б��Ч��
#
# greet_users
'''
def greet_users(names):
    """���б��е�ÿλ�û��������򵥵��ʺ�"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)
'''
#
# 8.4.1 �ں������޸��б��������������Ե��޸�
#
# printing_models ����һ������
'''
# ���ȴ���һ���б����а���һЩҪ��ӡ�����
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
'''
'''
# ģ���ӡÿ����ƣ�ֱ������ӡ�ˣ�֮���Ƶ��б�completed_models��
while unprinted_designs:
    cur_design = unprinted_designs.pop()
    
    #ģ������������3D��ӡģ�͵Ĺ���
    print("Printing model: " + cur_design)
    completed_models.append(cur_design)
# ��ʾ��ӡ�õ�����ģ��
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
'''
# printing_models ���� ��������
'''
def print_models(unprinted_designs, completed_models):
    """ 
    ģ���ӡÿ�� ���,ֱ�� û�� δ��ӡ�����Ϊֹ
    ��ӡÿ�� ��ƺ�,�������Ƶ��б� completed_ models �� 
    """ 
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # ģ������������ 3D ��ӡģ�͵Ĺ��� 
        print("Printing model: " + current_design) 
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """��ʾ��ӡ�õ�����ģ��"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
'''    
'''    
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
'''
#
# 8.4.2 ��ֹ�����޸��б�����������ԭʼ���б��� >����<
#                        �����б�� >����< ������ԭ�� 
#
# function_name(list_name(:))   # ��Ƭ��ʾ��[:]�����б�ĸ���
'''
print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)
'''
#
# 8.5 ��������������ʵ��
#
'''
def make_pizza(*toppings):   # ����һ����Ϊtoppings�Ŀ�Ԫ��
    """��ӡ�˿͵����������"""
    print("\nMaking a pizza with the follwing toppings:")
    for topping in toppings:
        print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
'''
#
# 8.5.1 ���ʹ��λ��ʵ�κ���������ʵ��
#
'''
def make_pizza(size, *toppings):   # ����һ����Ϊtoppings��>>��Ԫ��<<
    """����Ҫ����������"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the follwing toppings:")
    for topping in toppings:
        print(topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')
'''
#
# 8.5.2 ʹ�����������Ĺؼ���ʵ�� �� ��Ϊ�㲻��Ԥ֪�ᴫ������Щʲô��Ϣ
#
# user_profile
'''
def build_profile(first, last, **user_info): # ����һ����Ϊuser_info>>���ֵ�<<
    """����һ���ֵ䣬���а�������֪�����й��û���һ��"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('albert','einstein',
                            location='princeton',
                            field='physics')
print(user_profile)
'''
#
# 8.6 �������洢��ģ���У�import�������ʹ�õ���ģ���еĴ��� 
#     
#      >>>>>> ����ʵ��������鿴 pizza.py / making_pizzas.py <<<<<<
#
# 8.6.1 ��������ģ�� �� 1.pizza.py ; 2. making_pizzas.py �� import pizza
#                    3.ͨ��pizza.make_pizza(size,*toppings) ��ʽ����
#
#       ͨ�õ����﷨��module_name.function_name()
#
#
# 8.6.2 �����ض��ĺ��� ��1. from module_name import function_name
#                     1. from module_name import function_0, function_1,...
#
#
# 8.6.3 ʹ��as������ָ��������from module_ name import function_ name as fn
#
# 8.6.4 ʹ��as��ģ��ָ��������import module_name as mn
#
# 8.6.5 ����ģ���е����к�����from module_name import *
#
#
# 8.7 ������дָ�ϣ�
#     1.���β�ָ��Ĭ��ֵʱ���Ⱥ����߲�Ҫ�пո�
#       def function_ name( parameter_ 0, parameter_ 1=' default value')
#     2.���ں��������еĹؼ���ʵ�Σ�ҲӦ��ѭ����Լ����
#       function_name(value_0, parameter_1='value')
#     3.��������ĸ�ʽ
#
#       def function_name(
#               parameter_0, parameter_1, parameter_ 2,
#               parameter_3, parameter_4, parameter_5):
#           function body...
#
