'''
描述
输入1行句子（不多于200个单词，每个单词长度不超过100），只包含字母、空格和逗号。单词由至少一个连续的字母构成，空格和逗号都是单词间的间隔。

试输出第1个最长的单词和第1个最短单词。

输入
一行句子。
输出
两行输出：
第1行，第一个最长的单词。
第2行，第一个最短的单词。
样例输入
I am studying Programming language C in Peking University
样例输出
Programming
I
'''

ls=input().split()
l=[]
for item in ls:
    l.append(len(item))
maxw=l.index(max(l))
minw=l.index(min(l))
print("{}\n{}".format(ls[maxw],ls[minw]))
