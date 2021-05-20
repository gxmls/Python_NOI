'''
描述
给定一个字符，用它构造一个对角线长5个字符，倾斜放置的菱形。

输入
输入只有一行， 包含一个字符。
输出
该字符构成的菱形。
'''

s=input()
for i in range(1,6,2):
    print("{:^5}".format(s*i))
for i in range(2,5,2):
    print("{:^5}".format(s*(5-i)))
