'''
描述
津津上初中了。妈妈认为津津应该更加用功学习，所以津津除了上学之外，还要参加妈妈为她报名的各科复习班。
另外每周妈妈还会送她去学习朗诵、舞蹈和钢琴。但是津津如果一天上课超过八个小时就会不高兴，而且上得越久就会越不高兴。
假设津津不会因为其它事不高兴，并且她的不高兴不会持续到第二天。请你帮忙检查一下津津下周的日程安排，看看下周她会不会不高兴；如果会的话，哪天最不高兴。

输入
包括七行数据，分别表示周一到周日的日程安排。每行包括两个小于10的非负整数，用空格隔开，分别表示津津在学校上课的时间和妈妈安排她上课的时间。
输出
包括一行，这一行只包含一个数字。如果不会不高兴则输出0，如果会则输出最不高兴的是周几（用1, 2, 3, 4, 5, 6, 7分别表示周一，周二，周三，周四，周五，周六，周日）。
如果有两天或两天以上不高兴的程度相当，则输出时间最靠前的一天。
样例输入
5 3
6 2
7 2
5 3
5 4
0 4
0 6
样例输出
3
'''

ls=[]
for i in range(7):
    t=input().split()
    ls.append(eval(t[0])+eval(t[1]))
if max(ls)>8:
    print(ls.index(max(ls))+1)
else:
    print("0")

