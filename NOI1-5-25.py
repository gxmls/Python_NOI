'''
描述
一个十进制自然数,它的七进制与九进制表示都是三位数，且七进制与九进制的三位数码表示顺序正好相反。编程求此自然数,并输出显示。

输入
无。
输出
三行：
第一行是此自然数的十进制表示；
第二行是此自然数的七进制表示；
第三行是此自然数的九进制表示。
'''

def Sept(sc): #把十进制整数sc转换成七进制ds
    s7=''
    while sc//7!=0:
        s7+=str(sc%7)
        sc//=7
    s7+=str(sc%7)
    ds=int(s7[::-1])
    return ds

def Neuf(sn): #把十进制整数sn转换成九进制dn
    s9=''
    while sn//9!=0:
        s9+=str(sn%9)
        sn//=9
    s9+=str(sn%9)
    dn=int(s9[::-1])
    return dn

for i in range(49,343):
    if str(Sept(i))[::-1]==str(Neuf(i)):
        print("{:}\n{:}\n{:}".format(i,Sept(i),Neuf(i)))