'''
输入三个自然数N，i，j （1<=i<=N，1<=j<=N），输出在一个N*N格的棋盘中（行列均从1开始编号），与格子（i，j）同行、同列、同一对角线的所有格子的位置。
当n=4，i=2，j=3时，输出的结果是：
(2,1) (2,2) (2,3) (2,4)                        同一行上格子的位置
(1,3) (2,3) (3,3) (4,3)                        同一列上格子的位置
(1,2) (2,3) (3,4)                              左上到右下对角线上的格子的位置
(4,1) (3,2) (2,3) (1,4)                        左下到右上对角线上的格子的位置
输入
一行，三个自然数N，i，j，相邻两个数之间用单个空格隔开。1 <= N <= 10。
输出
四行：
第一行：从左到右输出同一行格子位置；
第二行：从上到下输出同一列格子位置；
第三行：从左上到右下输出同一对角线格子位置；
第四行：从左下到右上输出同一对角线格子位置。
其中每个格子位置用如下格式输出：(x,y)，x为行号，y为列号，采用英文标点，中间无空格。
相邻两个格子位置之间用单个空格隔开。
样例输入
4 2 3
样例输出
(2,1) (2,2) (2,3) (2,4)
(1,3) (2,3) (3,3) (4,3)
(1,2) (2,3) (3,4)
(4,1) (3,2) (2,3) (1,4)
'''

def Site(i,j): #返回格子坐标
    s="({},{})".format(i,j)
    return s
def P(ls):
    for i in range(len(ls)):
        if i<len(ls)-1:
            print(ls[i],end=' ')
        else:
            print(ls[i])

N,x,y=map(int,input().split())
l=[]
for i in range(1,N+1): #填充每个格子的坐标
    ls=[]
    for j in range(1,N+1):
        ls.append(Site(i,j))
    l.append(ls)
P(l[x-1]) #打印相同行的格子坐标
samecolumn=[]
for i in range(N):
    samecolumn.append(l[i][y-1])
P(samecolumn) #打印相同列的格子坐标
leftslide=[]
rightslide=[]
lx=x
ly=y
rx=x
ry=y
while lx>1 and ly>1: #找到左对角线最初始的位置
    lx-=1
    ly-=1
while lx<=N and ly<=N: #创建左对角线列表
    leftslide.append(Site(lx,ly))
    lx+=1
    ly+=1
P(leftslide)
while rx<N and ry>1: #找到右对角线最初始的位置
    rx+=1
    ry-=1
while rx<=N and ry<=N: #创建右对角线列表
    rightslide.append(Site(rx,ry))
    rx-=1
    ry+=1
P(rightslide)


