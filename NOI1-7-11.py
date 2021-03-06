'''
描述
R国和S国正陷入战火之中，双方都互派间谍，潜入对方内部，伺机行动。
历经艰险后，潜伏于S国的R国间谍小C终于摸清了S国军用密码的编码规则：
1、S国军方内部欲发送的原信息经过加密后在网络上发送，原信息的内容与加密后所的内容均由大写字母‘A’—‘Z’构成（无空格等其他字母）。
2、S国对于每个字母规定了对应的“密字”。加密的过程就是将原信息中的所有字母替换为其对应的“密字”。
3、每个字母只对应一个唯一的“密字”，不同的字母对应不同的“密字”。“密字”可以和原字母相同。
例如，若规定‘A’的密字为‘A’，‘B’的密字为‘C’（其他字母及密字略），则原信息“ABA”被加密为“ACA”。
现在，小C通过内线掌握了S国网络上发送的一条加密信息及其对应的原信息。小C希望能通过这条信息，破译S国的军用密码。
小C的破译过程是这样的：扫描原信息，对于原信息中的字母x（代表任一大写字母），找到其在加密信息中的对应大写字母y，并认为在密码里y是x的密字。如此进行下去直到停止于如下的某个状态：
1、所有信息扫描完毕，‘A’—‘Z’所有26个字母在原信息中均出现过并获得了相应的“密字”。
2、所有信息扫描完毕，但发现存在某个（或某些）字母在原信息中没有出现。
3、扫描中发现掌握的信息里有明显的自相矛盾或错误（违反S过密码的编码规则）。例如某条信息“XYZ”被翻译为“ABA”就违反了“不同字母对应不同密字”的规则。
在小C忙得头昏脑胀之际，R国司令部又发来电报，要求他翻译另外一条从S国刚刚截取到的加密信息。现在请你帮助小C：通过内线掌握的信息，尝试破译密码。然后利用破译的密码，翻译电报中的加密信息。

输入
共3行，每行为一个长度在1到100之间的字符串。
第1行为小C掌握的一条加密信息。
第2行为第1行的加密信息所对应的原信息。
第3行为R国司令部要求小C翻译的加密信息。
输入数据保证所有字符串仅由大写字母‘A’—‘Z’构成，且第1行长度与第2行相等。
输出
共1行。
若破译密码停止时出现2，3两种情况，请你输出“Failed”（不含引号，注意首字母大写，其它小写）。
否则请输出利用密码翻译电报中加密信息后得到的原信息。
样例输入
样例 #1：
AA
AB
EOWIE
样例 #2：
QWERTYUIOPLKJHGFDSAZXCVBN
ABCDEFGHIJKLMNOPQRSTUVWXY
DSLIEWO
样例 #3：
MSRTZCJKPFLQYVAWBINXUEDGHOOILSMIJFRCOPPQCEUNYDUMPP
YIZSDWAHLNOVFUCERKJXQMGTBPPKOIYKANZWPLLVWMQJFGQYLL
FLSO
样例输出
样例 #1：
Failed
样例#2：
Failed
样例#3：
NOIP
'''

code=input()
ori=input()
code2=input()
dic_code={}
for i in range(len(code)):
    if code[i] not in dic_code:
        dic_code[code[i]]=ori[i]
    else:
        if dic_code[code[i]]==ori[i]:
            continue
        else:
            break
'''
如果此处不判断密文是否重复，则以下样例无法正确输出"Failed"
样例5：
ABCDEFFGHIJKLMNOPQRSTUVWXYZ
ABCDEEFGHIJKLMNOPQRSTUVWXYZ
ASDSAF
Failed
'''
if len(set(dic_code.values()))!=26 or len(set(dic_code.keys()))!=26:
    print("Failed")
'''
此处必须要转换成集合去重，在判断，否则以下样例无法正确输出"Failed"
样例1：
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCCDEFGHIJKLMNOPQRSTUVWXY
ABDEF
Failed
'''
else:
    s=''
    for items in code2:
        s+=dic_code.get(items)
    print(s)


