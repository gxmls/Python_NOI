'''
描述
一个长度为n（n>0）的序列中存在“有趣的跳跃”当前仅当相邻元素的差的绝对值经过排序后正好是从1到(n-1)。
例如，1 4 2 3存在“有趣的跳跃”，因为差的绝对值分别为3,2,1。当然，任何只包含单个元素的序列一定存在“有趣的跳跃”。你需要写一个程序判定给定序列是否存在“有趣的跳跃”。

输入
一行，第一个数是n（0 < n < 3000），为序列长度，接下来有n个整数，依次为序列中各元素，各元素的绝对值均不超过1,000,000,000。
输出
一行，若该序列存在“有趣的跳跃”，输出"Jolly"，否则输出"Not jolly"。
样例输入
4 1 4 2 3
样例输出
Jolly
'''

ori=list(map(int,input().split()))
n=ori[0]
del ori[0]
ab=[]
ls=[]
for i in range(n-1):
    ab.append(abs(ori[i+1]-ori[i]))
for i in range(1,n):
    ls.append(i)
ab.sort()
if ab==ls:
    print("Jolly")
else:
    print("Not jolly")



