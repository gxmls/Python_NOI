'''
描述
给定一个5*5的矩阵，每行只有一个最大值，每列只有一个最小值，寻找这个矩阵的鞍点。
鞍点指的是矩阵中的一个元素，它是所在行的最大值，并且是所在列的最小值。
例如：在下面的例子中（第4行第1列的元素就是鞍点，值为8 ）。
11 3 5 6 9
12 4 7 8 10
10 5 6 9 11
8 6 4 7 2
15 10 11 20 25
输入
输入包含一个5行5列的矩阵
输出
如果存在鞍点，输出鞍点所在的行、列及其值，如果不存在，输出"not found"
样例输入
11 3 5 6 9
12 4 7 8 10
10 5 6 9 11
8  6 4 7 2
15 10 11 20 25
样例输出
4 1 8
'''

def MaxRow(ls):
    maxrow=[]
    for row in ls:
        maxrow.append(max(row))
    return maxrow
def MinColumn(ls):
    ls_column=[]
    mincolumn=[]
    for column in range(len(ls)):
        c=[]
        for row in range(len(ls[column])):
            c.append(ls[row][column])
        ls_column.append(c)
    for column in ls_column:
        mincolumn.append(min(column))
    return mincolumn

ls=[]
for i in range(5):
    ls.append(list(map(int,input().split())))
mr=MaxRow(ls)
mc=MinColumn(ls)
for i in range(5):
    for j in range(5):
        if ls[i][j]==mr[i] and ls[i][j]==mc[j]:
            print(i+1,j+1,ls[i][j]) #输出所在行和列，i,j需要+1
            break
    else:
        continue
    break #找到鞍点后退出整个循环
else:
    print("not found")








        

