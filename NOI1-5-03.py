'''
描述
给出一组样本数据，计算其均值。

输入
输入有两行，第一行包含一个整数n（n小于100），代表样本容量；第二行包含n个绝对值不超过1000的浮点数，代表各个样本数据。
输出
输出一行，包含一个浮点数，表示均值，精确到小数点后4位。
'''

n=eval(input())
s=0
sam=list(map(float,input().split()))
for i in range(n):
    s+=sam[i]
print("{:.4f}".format(s/n))


