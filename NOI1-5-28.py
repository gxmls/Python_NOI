'''
描述
给定一个整数，要求从个位开始分离出它的每一位数字。

输入
输入一个整数，整数在1到100000000之间。
输出
从个位开始按照从低位到高位的顺序依次输出每一位数字。数字之间以一个空格分开。
'''

n=input()
l=len(n)
for i in range(l):
    print(n[l-i-1],end=" ")