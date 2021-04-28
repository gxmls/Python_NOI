'''
描述
输入学生的人数，然后再输入每位学生的分数和姓名，求获得最高分数的学生的姓名。
输入
第一行输入一个正整数N（N <= 100），表示学生人数。接着输入N行，每行格式如下：
分数 姓名
分数是一个非负整数，且小于等于100；
姓名为一个连续的字符串，中间没有空格，长度不超过20。
数据保证最高分只有一位同学。
输出
获得最高分数同学的姓名。
样例输入
5
87 lilei
99 hanmeimei
97 lily
96 lucy
77 jim
样例输出
hanmeimei
'''

N=eval(input())
dic={}
for i in range(N):
    ls=input().split()
    dic[ls[1]]=dic.get(ls[1],eval(ls[0])) #如果不转换成eval()就会出错
items=list(dic.items())
items.sort(key=lambda x:x[1],reverse=True)
max_name,max_score=items[0]
print(max_name)

