'''
描述
给定正整数n，求不大于n的正整数的阶乘的和（即求1!+2!+3!+...+n!）

输入
输入有一行，包含一个正整数n（1 < n < 12）。
输出
输出有一行：阶乘的和。
样例输入
5
样例输出
153
'''

n=eval(input())
mul=1
Sum=0
for i in range(1,n+1):
    mul*=i
    Sum+=mul
print(Sum)
