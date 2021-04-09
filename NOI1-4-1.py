'''
描述
给定一个整数N，判断其正负。



输入
一个整数N(-109 <= N <= 109)
输出
如果N > 0, 输出positive;
如果N = 0, 输出zero;
如果N < 0, 输出negative
'''

N=int(input())
if N>0:
    print("positive")
elif N==0:
    print("zero")
else:
    print("negative")