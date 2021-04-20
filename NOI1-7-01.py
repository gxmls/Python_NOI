'''
描述
输入一行字符，统计出其中数字字符的个数。

输入
一行字符串，总长度不超过255。
输出
输出为1行，输出字符串里面数字字符的个数。
样例输入
Peking University is set up at 1898.
样例输出
4
'''

s=input()
count=0
for c in s:
    if c in ['0','1','2','3','4','5','6','7','8','9']:
        count+=1
print(count)
