'''
描述
一般我们用strcmp可比较两个字符串的大小，比较方法为对两个字符串从前往后逐个字符相比较（按ASCII码值大小比较），直到出现不同的字符或遇到'\0'为止。
如果全部字符都相同，则认为相同；如果出现不相同的字符，则以第一个不相同的字符的比较结果为准（注意：如果某个字符串遇到'\0'而另一个字符串还未遇到'\0'，则前者小于后者）。
但在有些时候，我们比较字符串的大小时，希望忽略字母的大小，例如"Hello"和"hello"在忽略字母大小写时是相等的。请写一个程序，实现对两个字符串进行忽略字母大小写的大小比较。

输入
输入为两行，每行一个字符串，共两个字符串。（每个字符串长度都小于80）
输出
如果第一个字符串比第二个字符串小，输出一个字符"<"；
如果第一个字符串比第二个字符串大，输出一个字符">"；
如果两个字符串相等，输出一个字符"="。
样例输入
Hello, how are you?
hello, How are you?
样例输出
=
'''

s1=input()
s2=input()
sn1=s1.lower()
sn2=s2.lower()
if sn1==sn2:
    print("=")
else:
    if len(sn1)<=len(sn2):
        for i in range(len(sn1)):
            if ord(sn1[i])>ord(sn2[i]):
                print(">")
                break
            elif ord(sn1[i])<ord(sn2[i]):
                print("<")
                break
            else:
                continue
        else:
            print("<")
    else:
        for i in range(len(sn2)):
            if ord(sn1[i])>ord(sn2[i]):
                print(">")
                break
            elif ord(sn1[i])<ord(sn2[i]):
                print("<")
                break
            else:
                continue
        else:
            print(">")
        


