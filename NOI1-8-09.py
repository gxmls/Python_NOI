'''
描述
计算两个矩阵的乘法。n*m阶的矩阵A乘以m*k阶的矩阵B得到的矩阵C 是n*k阶的，且C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + …… +A[i][m-1]*B[m-1][j](C[i][j]表示C矩阵中第i行第j列元素)。
输入
第一行为n, m, k，表示A矩阵是n行m列，B矩阵是m行k列，n, m, k均小于100
然后先后输入A和B两个矩阵，A矩阵n行m列，B矩阵m行k列，矩阵中每个元素的绝对值不会大于1000。
输出
输出矩阵C，一共n行，每行k个整数，整数之间以一个空格分开。
样例输入
3 2 3
1 1
1 1
1 1
1 1 1
1 1 1
样例输出
2 2 2
2 2 2
2 2 2
'''
n,m,k=map(int,input().split())
A=[]
B=[]
C=[[0 for i in range(k)] for j in range(n)] #初始化二维数组不能写成C=[[0]*k]*n,这样不是真正的二维数组
for i in range(n):
    A.append(list(map(int,input().split())))
for i in range(m):
    B.append(list(map(int,input().split())))
for i in range(n):
    for j in range(k):
        for x in range(m):
            C[i][j]+=A[i][x]*B[x][j]
    for j in range(k):
        if j==k-1:
            print(C[i][j])
        else:
            print(C[i][j],end=' ')

        




