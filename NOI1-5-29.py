'''
描述
给定一个整数，请将该数各个位上数字反转得到一个新数。新数也应满足整数的常见形式，即除非给定的原数为零，否则反转后得到的新数的最高位数字不应为零（参见样例2）。

输入
输入共 1 行，一个整数N。

-1,000,000,000 ≤ N≤ 1,000,000,000。
输出
输出共 1 行，一个整数，表示反转后的新数。
'''

N=eval(input())
new=''
if N>0:
    l=len(str(N))
    for i in range(l):
        new+=str(N)[l-i-1]
    print(int(new))
elif N<0:
    l=len(str(N))-1
    for i in range(l):
        new+=str(N)[l-i]
    print(0-int(new))
else:
    print(0)

