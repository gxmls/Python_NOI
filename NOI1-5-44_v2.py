'''
描述
输入一个正整数n，求第n小的质数。

输入
一个不超过10000的正整数n。
输出
第n小的质数。
样例输入
10
样例输出
29
'''

n=eval(input())
count=0
test=1
while count<n:
    test+=1
    for i in range(2,int(test**0.5)+1): #这里用int(test**0.5)是为了将循环数减半，否则循环数太大
        if test%i==0:
            break
    else: #如果上方for循环被break，此处的else不被执行，当穷尽列表循环结束时才被执行
        count+=1
print(test)
    

