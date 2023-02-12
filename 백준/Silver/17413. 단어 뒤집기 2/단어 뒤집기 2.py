import sys
input = sys.stdin.readline

S = input().strip()
ans = ''
no = False
temp = ''
for i in S:
    if i == '<':
        no = True
        ans += temp[::-1]
        ans += '<'
        temp = ''
    elif i == '>':
        no = False
        ans += '>'
    elif i == ' ':
        ans += temp[::-1]
        ans += ' '
        temp = ''
    else:
        if not no:
            temp += i
        elif no:
            ans += i
if len(S) != len(ans):
    ans += temp[::-1]
print(ans)