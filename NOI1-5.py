'''
描述
读入一个双精度浮点数，保留12位小数，输出这个浮点数。

输入
只有一行，一个双精度浮点数。
输出
也只有一行，保留12位小数的浮点数。
'''

f1=eval(input())
print("{:.12f}".format(f1))