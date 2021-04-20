'''
描述
已知正整数k满足2<=k<=9，现给出长度最大为30位的十进制非负整数c，求所有能整除c的k。

输入
一个非负整数c，c的位数<=30。
输出
若存在满足 c%k == 0 的k，从小到大输出所有这样的k，相邻两个数之间用单个空格隔开；若没有这样的k，则输出"none"。
样例输入
30
样例输出
2 3 5 6 
'''

c=eval(input())
ls=[]
for i in range(2,10):
    if c%i==0:
        ls.append(i)
if len(ls)>=1:
    for i in ls:
        print(i,end=" ")
else:
    print('none')
    