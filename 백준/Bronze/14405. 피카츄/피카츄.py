import sys
input = sys.stdin.readline

s = input().strip()
i = 0
while i < len(s):
    if s[i] == 'p':
        if s[i:i + 2] != 'pi':
            break
        i += 2
    elif s[i] == 'k':
        if s[i:i + 2] != 'ka':
            break
        i += 2
    elif s[i] == 'c':
        if s[i:i + 3] != 'chu':
            break
        i += 3
    else:
        break
print('YES' if i == len(s) else 'NO')