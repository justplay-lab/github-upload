#
# 实例1 —— 编译单词的字母
#
for letter in 'Python':
    print('当前字母： ' + letter)
'''output
当前字母： P
当前字母： y
当前字母： t
当前字母： h
当前字母： o
当前字母： n
'''
#
# 实例2 —— 通过序列索引迭代
#
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果： ' + fruits[index])
'''output
当前水果： banana
当前水果： apple
当前水果： mango
'''
#
# 实例4 —— 基本for循环
#
for num in range(1, 10):
    print(num)
'''output
1
2
3
4
5
6
7
8
9
'''
#
# 实例4 —— 循环使用 else 语句
#
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print(num, '是一个质数')
'''output
10 等于 2 * 5
11 是一个质数
12 等于 2 * 6
13 是一个质数
14 等于 2 * 7
15 等于 3 * 5
16 等于 2 * 8
17 是一个质数
18 等于 2 * 9
19 是一个质数
'''