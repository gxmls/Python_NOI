'''
描述
石头剪刀布是常见的猜拳游戏。石头胜剪刀，剪刀胜布，布胜石头。如果两个人出拳一样，则不分胜负。

一天，小A和小B正好在玩石头剪刀布。已知他们的出拳都是有周期性规律的，比如：“石头-布-石头-剪刀-石头-布-石头-剪刀……”，
就是以“石头-布-石头-剪刀”为周期不断循环的。请问，小A和小B比了N轮之后，谁赢的轮数多？

输入
输入包含三行。
第一行包含三个整数：N，NA，NB，分别表示比了N轮，小A出拳的周期长度，小B出拳的周期长度。0 < N,NA,NB < 100。
第二行包含NA个整数，表示小A出拳的规律。
第三行包含NB个整数，表示小B出拳的规律。
其中，0表示“石头”，2表示“剪刀”，5表示“布”。相邻两个整数之间用单个空格隔开。
输出
输出一行，如果小A赢的轮数多，输出A；如果小B赢的轮数多，输出B；如果两人打平，输出draw。
样例输入
10 3 4
0 2 5
0 5 0 2
样例输出
A
'''

N,NA,NB=map(int,input().split())
listA=list(map(int,input().split()))
listB=list(map(int,input().split()))
listA*=N//NA
for i in range(1,N%NA+1):
    listA.append(listA[i-1])
listB*=N//NB
for i in range(1,N%NB+1):
    listB.append(listB[i-1])
c_A=0
c_B=0
for i in range(N):
    if listA[i]==0 and listB[i]==2:
        c_A+=1
        c_B-=1
    elif listA[i]==2 and listB[i]==5:
        c_A+=1
        c_B-=1
    elif listA[i]==5 and listB[i]==0:
        c_A+=1
        c_B-=1
    elif listB[i]==0 and listA[i]==2:
        c_A-=1
        c_B+=1
    elif listB[i]==2 and listA[i]==5:
        c_A-=1
        c_B+=1
    elif listB[i]==5 and listA[i]==0:
        c_A-=1
        c_B+=1
    else:
        pass
if c_A>c_B:
    print('A')
elif c_A<c_B:
    print('B')   
else:
    print("draw")



