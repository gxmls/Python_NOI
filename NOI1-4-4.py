'''
描述
任意输入一个字符，判断其ASCII是否是奇数，若是，输出YES，否则，输出NO
例如，字符A的ASCII值是65，则输出YES，若输入字符B(ASCII值是66)，则输出NO

输入
输入一个字符
输出
如果其ASCII值为奇数，则输出YES，否则，输出NO
'''

s=input()
if ord(s)%2==1:
    print("YES")
else:
    print("NO")