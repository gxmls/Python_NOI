'''
描述
给出两幅相同大小的黑白图像（用0-1矩阵）表示，求它们的相似度。
说明：若两幅图像在相同位置上的像素点颜色相同，则称它们在该位置具有相同的像素点。两幅图像的相似度定义为相同像素点数占总像素点数的百分比。
输入
第一行包含两个整数m和n，表示图像的行数和列数，中间用单个空格隔开。1 <= m <= 100, 1 <= n <= 100。
之后m行，每行n个整数0或1，表示第一幅黑白图像上各像素点的颜色。相邻两个数之间用单个空格隔开。
之后m行，每行n个整数0或1，表示第二幅黑白图像上各像素点的颜色。相邻两个数之间用单个空格隔开。
输出
一个实数，表示相似度（以百分比的形式给出），精确到小数点后两位。
样例输入
3 3
1 0 1
0 0 1
1 1 0
1 1 0
0 0 1
0 0 1
样例输出
44.44
'''

m,n=map(int,input().split())
fig1=[]
fig2=[]
for i in range(m):
    fig1.append(list(map(int,input().split())))
for i in range(m):
    fig2.append(list(map(int,input().split())))
count=0
for i in range(m):
    for j in range(n):
        if fig1[i][j]==fig2[i][j]:
            count+=1
print("{:.2f}".format(count/(m*n)*100))



