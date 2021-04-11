'''
描述
给定若干个四位数，求出其中满足以下条件的数的个数：

个位数上的数字减去千位数上的数字，再减去百位数上的数字， 再减去十位数上的数字的结果大于零。

输入
输入为两行，第一行为四位数的个数n，第二行为n个的四位数，数与数之间以一个空格分开。(n <= 100)
输出
输出为一行，包含一个整数，表示满足条件的四位数的个数。
'''

n=eval(input())
m=list(map(int,input().split()))
count=0
for i in range(n):
    s=str(m[i])
    if (eval(s[-1])-eval(s[0])-eval(s[1])-eval(s[-2]))>0:
        count+=1
print(count)
