'''
描述
给定一个5*5的矩阵（数学上，一个r×c的矩阵是一个由r行c列元素排列成的矩形阵列），将第n行和第m行交换，输出交换后的结果。

输入
输入共6行，前5行为矩阵的每一行元素,元素与元素之间以一个空格分开。
第6行包含两个整数m、n，以一个空格分开。（1 <= m,n <= 5）
输出
输出交换之后的矩阵，矩阵的每一行元素占一行，元素之间以一个空格分开。
样例输入
1 2 2 1 2
5 6 7 8 3
9 3 0 5 3
7 2 1 4 6
3 0 8 2 4
1 5
样例输出
3 0 8 2 4
5 6 7 8 3
9 3 0 5 3
7 2 1 4 6
1 2 2 1 2
'''

def P(ls):
    for i in range(4):
        print(ls[i],end=' ')
    print(ls[4])
ls=[]
for i in range(5):
    ls.append(list(map(int,input().split()))) 
m,n=map(int,input().split())
for i in range(5):
    if i==m-1:
        P(ls[n-1])
    elif i==n-1:
        P(ls[m-1])
    else:
        P(ls[i])
       
