'''
描述
对于一个字符串来说，定义一次循环移位操作为：将字符串的第一个字符移动到末尾形成新的字符串。

给定两个字符串s1和s2，要求判定其中一个字符串是否是另一字符串通过若干次循环移位后的新字符串的子串。
例如CDAA是由AABCD两次移位后产生的新串BCDAA的子串，而ABCD与ACBD则不能通过多次移位来得到其中一个字符串是新串的子串。

输入
一行，包含两个字符串，中间由单个空格隔开。字符串只包含字母和数字，长度不超过30。
输出
如果一个字符串是另一字符串通过若干次循环移位产生的新串的子串，则输出true，否则输出false。
样例输入
AABCD CDAA
样例输出
true
'''

s1,s2=input().split()
sn1=s1
sn2=s2
for i in range(len(s1)):
    sn1+=s1[i]
for i in range(len(s2)):
    sn2+=s2[i]
if len(s1)<=len(s2) and s1 in sn2:
    print("ture")
elif len(s2)<=len(s1) and s2 in sn1:
    print("ture")
else:
    print("false")