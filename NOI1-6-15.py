'''
描述
用高精度计算出S=1!+2!+3!+…+n!（n≤50）

其中“!”表示阶乘，例如：5!=5*4*3*2*1。

输入正整数N，输出计算结果S。

输入
一个正整数N。
输出
计算结果S。
样例输入
5
样例输出
153
'''

def fact(n): 
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=eval(input())
s=0
for i in range(1,n+1):
    s+=fact(i)
print(s)
