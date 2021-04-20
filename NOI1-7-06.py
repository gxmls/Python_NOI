'''
描述
给定一个不包含空白符的字符串，请判断是否是C语言合法的标识符号（注：题目保证这些字符串一定不是C语言的保留字）。

C语言标识符要求：

1. 非保留字；

2. 只包含字母、数字及下划线（“_”）。

3. 不以数字开头。

输入
一行，包含一个字符串，字符串中不包含任何空白字符，且长度不大于20。
输出
一行，如果它是C语言的合法标识符，则输出yes，否则输出no。
样例输入
RKPEGX9R;TWyYcp
样例输出
no
'''

s=input()
if s.isidentifier(): #s.isidentifier()用来判断字符串是否为合法标识符
    print('yes')
else:
    print('no')

