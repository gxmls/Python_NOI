'''
描述
输入一个浮点数，输出这个浮点数的绝对值。

输入
输入一个浮点数，其绝对值不超过10000。
输出
输出这个浮点数的绝对值，保留到小数点后两位。
'''

n=eval(input())
print("{:.2f}".format(abs(n)))