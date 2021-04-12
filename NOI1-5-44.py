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
def pnum(p):
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
    return True
n=eval(input())
count=0
test=1
while count<n:
    test+=1
    if pnum(test):
        count+=1
print(test)



     

