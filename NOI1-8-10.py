'''
描述
输入一个n行m列的矩阵A，输出它的转置AT。
输入
第一行包含两个整数n和m，表示矩阵A的行数和列数。1 <= n <= 100，1 <= m <= 100。
接下来n行，每行m个整数，表示矩阵A的元素。相邻两个整数之间用单个空格隔开，每个元素均在1~1000之间。
输出
m行，每行n个整数，为矩阵A的转置。相邻两个整数之间用单个空格隔开。
样例输入
3 3
1 2 3
4 5 6
7 8 9
样例输出
1 4 7
2 5 8
3 6 9
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
for i in range(m):
    for j in range(n-1):
        print(AT[i][j],end=' ')
    print(AT[i][n-1])


