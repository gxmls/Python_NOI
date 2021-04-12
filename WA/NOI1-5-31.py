'''
描述
假设有N盏灯(N为不大于5000的正整数)，从1到N按顺序依次编号，初始时全部处于开启状态；有M个人(M为不大于N的正整数)也从1到M依次编号。

第一个人（1号）将灯全部关闭，第二个人（2号）将编号为2的倍数的灯打开，第三个人（3号）将编号为3的倍数的灯做相反处理（即，将打开的灯关闭，将关闭的灯打开）。
依照编号递增顺序，以后的人都和3号一样，将凡是自己编号倍数的灯做相反处理。

请问：当第M个人操作之后，哪几盏灯是关闭的，按从小到大输出其编号，其间用逗号间隔。

输入
输入正整数N和M，以单个空格隔开。
输出
顺次输出关闭的灯的编号，其间用逗号间隔。
'''

N,M=map(int,input().split())
on=[1]*N
off=[0]*N
for j in range(1,M+1):
    for i in range(1,N+1):
        if i%j==0:
            on[i-1],off[i-1]=off[i-1],on[i-1]
s=''
for i in range(1,N+1):
    if on[i-1]==0:
        s+=str(i)
print(','.join(s))

#提交OpenJudge评阅系统后，超时不得分        
        
