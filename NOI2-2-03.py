'''
描述
给出一个正整数a，要求分解成若干个正整数的乘积，即a = a1 * a2 * a3 * ... * an，并且1 < a1 <= a2 <= a3 <= ... <= an，
问这样的分解的种数有多少。注意到a = a也是一种分解。
输入
第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数a (1 < a < 32768)
输出
n行，每行输出对应一个输入。输出应是一个正整数，指明满足要求的分解的种数
样例输入
2
2
20
样例输出
1
4
'''

def factor(n,p):
    sum=1
    for i in range(p,int(n**0.5)+1):
        if n%i==0:
            sum+=factor(n//i,i)
    return sum

n=eval(input())
s=[]
for i in range(n):
    s.append(eval(input()))
for i in range(n):
    print(factor(s[i],2))













