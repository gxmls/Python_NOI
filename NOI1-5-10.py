'''
描述
将正整数 m 和 n 之间（包括 m 和 n）能被 17 整除的数累加。其中，0 < m < n < 1000。

输入
一行，包含两个整数m和n，其间，以一个空格间隔。
输出
输出一行，包行一个整数，表示累加的结果。
'''

m,n=map(int,input().split())
s=0
if 0<m<n<1000:
    for i in range(m,n+1):
        if i%17==0:
            s+=i
        else:
            pass
else:
    pass
print(s)
