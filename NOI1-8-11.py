'''
描述
输入一个n行m列的黑白图像，将它顺时针旋转90度后输出。
输入
第一行包含两个整数n和m，表示图像包含像素点的行数和列数。1 <= n <= 100，1 <= m <= 100。
接下来n行，每行m个整数，表示图像的每个像素点灰度。相邻两个整数之间用单个空格隔开，每个元素均在0~255之间。
输出
m行，每行n个整数，为顺时针旋转90度后的图像。相邻两个整数之间用单个空格隔开。
样例输入
3 3
1 2 3
4 5 6
7 8 9
样例输出
7 4 1
8 5 2
9 6 3
'''

A=[]
n,m=map(int,input().split())
for i in range(n):
    A.append(list(map(int,input().split())))
AT=[]
for j in range(m):
    c=[]
    for i in range(n):
        c.append(A[i][j])
    AT.append(c)
for col in AT: #顺时针旋转90度就是将转置后的二维数组的每行再反向输出
    for c in col[::-1][:-1]:
        print(c,end=' ')
    print(col[::-1][-1])

