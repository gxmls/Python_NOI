'''
描述
输入一个字符串，以回车结束（字符串长度<=100）。该字符串由若干个单词组成，单词之间用一个空格隔开，所有单词区分大小写。
现需要将其中的某个单词替换成另一个单词，并输出替换之后的字符串。
输入
输入包括3行，
第1行是包含多个单词的字符串 s;
第2行是待替换的单词a(长度 <= 100);
第3行是a将被替换的单词b(长度 <= 100).

s, a, b 最前面和最后面都没有空格.
输出
输出只有 1 行，将s中所有单词a替换成b之后的字符串。
样例输入
You want someone to help you
You
I
样例输出
I want someone to help you
'''

s=input()
a=input()
b=input()
sn=''
ls=list(s.split())
for i in range(len(ls)):
    if ls[i]==a: #题目要求全部替换，如果用index()只能找到第一个
        ls[i]=b
    else:
        continue
for item in ls:
    print(item,end=' ')



