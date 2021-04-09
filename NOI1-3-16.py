'''
描述
已知线段的两个端点的坐标A（Xa,Ya），B（Xb，Yb），求线段AB的长度。

输入
共两行。
第一行是两个实数Xa，Ya，即A的坐标。
第二行是两个实数Xb，Yb，即B的坐标。
输入中所有实数的绝对值均不超过10000。
输出
一个实数，即线段AB的长度，保留到小数点后3位。
'''

xa,ya=map(float,input().split())
xb,yb=map(float,input().split())
s=(abs(xb-xa)**2+abs(yb-ya)**2)**0.5
print("{:.3f}".format(s))