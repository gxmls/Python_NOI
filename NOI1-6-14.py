'''
描述
求10000以内n的阶乘。

输入
只有一行输入，整数n（0<=n<=10000）。
输出
一行，即n!的值。
'''

def fact(n): #此题用递归函数会计算超时
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=eval(input())
F=1
for i in range(1,n+1):
    F*=i
print(F)