'''
描述
输入两个n行m列的矩阵A和B，输出它们的和A+B。
输入
第一行包含两个整数n和m，表示矩阵的行数和列数。1 <= n <= 100，1 <= m <= 100。
接下来n行，每行m个整数，表示矩阵A的元素。
接下来n行，每行m个整数，表示矩阵B的元素。
相邻两个整数之间用单个空格隔开，每个元素均在1~1000之间。
输出
n行，每行m个整数，表示矩阵加法的结果。相邻两个整数之间用单个空格隔开。
样例输入
3 3
1 2 3
1 2 3
1 2 3
1 2 3
4 5 6
7 8 9
样例输出
2 4 6
5 7 9
8 10 12
'''

n,m=map(int,input().split())
A=[]
B=[]
for i in range(n):
    A.append(list(map(int,input().split())))
for i in range(n):
    B.append(list(map(int,input().split())))
for i in range(n):
    s=[]
    for j in range(m):
        s.append(A[i][j]+B[i][j])
    for i in range(m):
        if i==m-1:
            print(s[i])
        else:
            print(s[i],end=' ')
   

    

    







