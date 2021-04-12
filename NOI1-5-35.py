'''
描述
利用公式e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n! 求e 。
输入
输入只有一行，该行包含一个整数n（2<=n<=15），表示计算e时累加到1/n！。
输出
输出只有一行，该行包含计算出来的e的值，要求打印小数点后10位。
样例输入
10
样例输出
2.7182818011
'''

n=eval(input())
mul=1
e=1
for i in range(1,n+1):
    mul*=i
    e+=1/mul
print("{:.10f}".format(e))