'''
描述
给定3个整数a、b、c，计算表达式(a+b)/c的值，/是整除运算。

输入
输入仅一行，包括三个整数a、b、c, 数与数之间以一个空格分开。(－10,000 < a,b,c < 10,000, c不等于0)
输出
输出一行，即表达式的值。
'''

a,b,c=map(int,input().split())
if -10000<a and b and c<10000 and c!=0:
    print(int((a+b)/c)) #如果用(a+b)//c 结果不对
else:
    pass
