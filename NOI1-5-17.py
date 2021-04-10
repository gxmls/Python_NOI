'''
描述
菲波那契数列是指这样的数列: 数列的第一个和第二个数都为1，接下来每个数都等于前面2个数之和。
给出一个正整数k，要求菲波那契数列中第k个数是多少。

输入
输入一行，包含一个正整数k。（1 <= k <= 46）
输出
输出一行，包含一个正整数，表示菲波那契数列中第k个数的大小
'''
s=[1,1]
k=eval(input())
for i in range(2,k):
    s.append(s[i-2]+s[i-1])
print(s[k-1])


