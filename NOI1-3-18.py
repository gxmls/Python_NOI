'''
描述
给出一个等差数列的前两项a1，a2，求第n项是多少。
等差数列公式 an=a1+(n-1)*d (d为差值)
输入
一行，包含三个整数a1，a​2，n。-100 <= a1,a​2 <= 100，0 < n <= 1000。
输出
一个整数，即第n项的值。
'''

a1,a2,n=map(int,input().split())
print(a1+(n-1)*(a2-a1))