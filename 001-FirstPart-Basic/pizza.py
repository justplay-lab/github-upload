#coding=gbk
#
def make_pizza(size, *toppings):   # 创建一个名为toppings的>>空元组<<
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the follwing toppings:")
    for topping in toppings:
        print(topping)
