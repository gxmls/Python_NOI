'''
描述
某程序员开始工作，年薪N万，他希望在中关村公馆买一套60平米的房子，现在价格是200万，
假设房子价格以每年百分之K增长，并且该程序员未来年薪不变，且不吃不喝，不用交税，每年所得N万全都积攒起来，
问第几年能够买下这套房子？（第一年年薪N万，房价200万）

输入
一行，包含两个正整数N（10 <= N <= 50）, K（1 <= K <= 20），中间用单个空格隔开。
输出
如果在第20年或者之前就能买下这套房子，则输出一个整数M，表示最早需要在第M年能买下，否则输出Impossible。
'''

N,K=map(int,input().split())
k=1+K/100
year=1
while N*year<200*pow(k,(year-1)):
    year+=1
    if year>20: #如果不判断年份，工资跟不上房价就会数据溢出
        break
    else:
        pass
if year<=20:
    print(year)
else:
    print('Impossible')
