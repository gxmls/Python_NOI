'''
描述
输入两个整数，比较它们的大小。

输入
一行，包含两个整数x和y，中间用单个空格隔开。
0 <= x < 2^32, -2^31 <= y < 2^31。
输出
一个字符。
若x > y，输出 > ；
若x = y，输出 = ；
若x < y，输出 < ；
'''

x,y=map(int,input().split())
if x>y:
    print(">")
elif x==y:
    print("=")
else:
    print("<")
    