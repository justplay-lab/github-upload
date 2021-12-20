#coding=gbk
import json

def get_stored_username():
    """����洢���û������ͽػ���"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj).strip()
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """��ʾ�û������û���"""
    username = input("What is your name?\t")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def verify_user(username):
    """ѯ���û���Ta���û����Ƿ���ȷ"""
    handled_answer = ""
    input_active = True
    while input_active:
        answer = input("Is " + username.title() + " your username? " +
                    "(please enter y or n !)\t")
        handled_answer = answer.strip()
        correct_answers = ['y', 'Y', 'n', 'N']
        if handled_answer in correct_answers:
            input_active = False   
        else:
            input_active = True
            
        # ~ print(input_active)
        continue
            
    return handled_answer
            
def greet_user():
    username = get_stored_username()
    answer = verify_user(username)  # y or n
    if answer == 'y':
        print("Welcome back, " + username.title() + "!")
    elif answer == 'n':
        username = get_new_username()
        print("We'll remember you when you come back, " +
               username.title() + "!")
    else:
        print("Error msg, the answer should be 'y' or 'n'!!!")
        

'''
def greet_user():
    """�ʺ��û�����ָ������"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name?\t")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when your come back, "
                  + username.title() + "!")
    else:
        print("Welcome back, " + username.title() + "!")
'''
