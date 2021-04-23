'''
描述
给定一个单词，如果该单词以er、ly或者ing后缀结尾， 则删除该后缀（题目保证删除后缀后的单词长度不为0）， 否则不进行任何操作。

输入
输入一行，包含一个单词（单词中间没有空格，每个单词最大长度为32）。
输出
输出按照题目要求处理后的单词。
样例输入
referer
样例输出
refer
'''

word=input()
if len(word)>=3 and (word[-2:]=='er' or word[-2:]=='ly'):
    print(word[:-2])
elif len(word)>=4 and word[-3:]=='ing':
    print(word[:-3])
else:
    print(word)