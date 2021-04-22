'''
描述
判断两个由大小写字母和空格组成的字符串在忽略大小写，且忽略空格后是否相等。

输入
两行，每行包含一个字符串。
输出
若两个字符串相等，输出YES，否则输出NO。
样例输入
a A bb BB ccc CCC
Aa BBbb CCCccc
'''

s1=input().split()
s2=input().split()
sn1=''
sn2=''
for item in s1:
    sn1+=item
for item in s2:
    sn2+=item
if sn1.lower()==sn2.lower():
    print("YES")
else:
    print("NO")
