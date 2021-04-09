'''
描述
对于半径为r的球，其体积的计算公式为V=4/3*πr3，这里取π= 3.14。

现给定r，求V。

输入
输入为一个不超过100的非负实数，即球半径，类型为double。
输出
输出一个实数，即球的体积，保留到小数点后2位。
'''

r=eval(input())
print("{:.2f}".format(4/3*3.14*pow(r,3)))