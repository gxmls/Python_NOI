'''
描述
给定n*n由0和1组成的矩阵，如果矩阵的每一行和每一列的1的数量都是偶数，则认为符合条件。
你的任务就是检测矩阵是否符合条件，或者在仅改变一个矩阵元素的情况下能否符合条件。
"改变矩阵元素"的操作定义为0变成1或者1变成0。
输入
输入n + 1行，第1行为矩阵的大小n(0 < n < 100)，以下n行为矩阵的每一行的元素，元素之间以一个空格分开。
输出
如果矩阵符合条件，则输出OK；
如果矩阵仅改变一个矩阵元素就能符合条件，则输出需要改变的元素所在的行号和列号，以一个空格分开。
如果不符合以上两条，输出Corrupt。
样例输入
样例输入1
4
1 0 1 0
0 0 0 0
1 1 1 1
0 1 0 1
样例输入2
4
1 0 1 0
0 0 1 0
1 1 1 1
0 1 0 1
样例输入3
4
1 0 1 0
0 1 1 0
1 1 1 1
0 1 0 1
样例输出
样例输出1
OK
样例输出2
2 3
样例输出3
Corrupt
'''
def Judge(ls):
    n=len(ls)
    count_row=[]
    count_column=[0]*n
    for i in range(n):
        cr=0
        for j in range(n):
            if ls[i][j]==1:
                cr+=1
            if ls[j][i]==1:
                count_column[i]+=1
        if cr%2!=0: #增加条件，减少循环数
            return False
            break
        else:
            count_row.append(cr)
        if count_column[i]%2!=0: #增加条件，减少循环数
            return False
            break
    else:
        return True

n=eval(input())
ls=[]
for i in range(n):
    ls.append(list(map(int,input().split())))
if Judge(ls):
    print("OK")
else:
    for i in range(n):
        for j in range(n):
            if ls[i][j]==1:
                ls[i][j]=0
                if Judge(ls):
                    print("{} {}".format(i+1,j+1))
                    break
                else:
                    ls[i][j]=1
            else:
                ls[i][j]=1
                if Judge(ls):
                    print("{} {}".format(i+1,j+1))
                    break
                else:
                    ls[i][j]=0
        else: 
            continue
        break #如果for j in range(n)被break，执行此条语句跳出整个循环
    else:
        print("Corrupt")


