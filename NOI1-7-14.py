'''
描述
把一个字符串中所有出现的大写字母都替换成小写字母，同时把小写字母替换成大写字母。

输入
输入一行：待互换的字符串。
输出
输出一行：完成互换的字符串（字符串长度小于80）。
样例输入
If so, you already have a Google Account. You can sign in on the right. 
样例输出
iF SO, YOU ALREADY HAVE A gOOGLE aCCOUNT. yOU CAN SIGN IN ON THE RIGHT. 
'''

s=input()
sn=''
for c in s:
    if 'A'<=c<='Z':
        sn+=c.lower()
    elif 'a'<=c<='z':
        sn+=c.upper()
    else:
        sn+=c
print(sn)