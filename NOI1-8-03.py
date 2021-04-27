'''
描述
输入一个整数矩阵，计算位于矩阵边缘的元素之和。所谓矩阵边缘的元素，就是第一行和最后一行的元素以及第一列和最后一列的元素。

输入
第一行分别为矩阵的行数m和列数n（m < 100，n < 100），两者之间以一个空格分开。
接下来输入的m行数据中，每行包含n个整数，整数之间以一个空格分开。
输出
输出对应矩阵的边缘元素和
样例输入
3 3
3 4 1
3 7 1
2 0 1
样例输出
15
'''

m,n=map(int,input().split())
ls=[]
for i in range(m):
    ls.append(list(map(int,input().split())))
s=0
for i in range(m):
    for j in range(n):
        if i==0 or j==0:
            s+=ls[i][j]
        elif i==m-1 or j==n-1:
            s+=ls[i][j]
print(s)

