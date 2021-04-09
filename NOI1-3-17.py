'''
描述
平面上有一个三角形，它的三个顶点坐标分别为(x1, y1), (x2, y2), (x3, y3)，那么请问这个三角形的面积是多少。
海伦公式：A=(s*(s-a)*(s-b)*(s-c))**0.5，其中s=1/2*(a+b+c)

输入
输入仅一行，包括6个单精度浮点数，分别对应x1, y1, x2, y2, x3, y3。
输出
输出也是一行，输出三角形的面积，精确到小数点后两位。
'''

def len(l1,l2,l3,l4):
    l=(abs(l3-l1)**2+abs(l4-l2)**2)**0.5
    return l
    
x1,y1,x2,y2,x3,y3=map(float,input().split())
a=len(x1,y1,x2,y2)
b=len(x1,y1,x3,y3)
c=len(x2,y2,x3,y3)
s=1/2*(a+b+c)
A=(s*(s-a)*(s-b)*(s-c))**0.5
print("{:.2f}".format(A))