'''
描述
输入两个字符串，验证其中一个串是否为另一个串的子串。

输入
输入两个字符串， 每个字符串占一行，长度不超过200且不含空格。
输出
若第一个串s1是第二个串s2的子串，则输出(s1) is substring of (s2)
否则，若第二个串s2是第一个串s1的子串，输出(s2) is substring of (s1)
否则，输出 No substring。
样例输入
abc
dddncabca
样例输出
abc is substring of dddncabca
'''

s1=input()
s2=input()
if s1 in s2:
    print("{} is substring of {}".format(s1,s2))
elif s2 in s1:
    print("{} is substring of {}".format(s2,s1))
else:
    print("No substring")