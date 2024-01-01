import sys
input = sys.stdin.readline

n = input().strip()
if len(n) == 4:
    a, b = int(n[:2]), int(n[2:])
elif len(n) == 3:
    if n[1] == '0':
        a, b = int(n[:2]), int(n[-1])
    else:
        a, b = int(n[0]), int(n[1:])
else:
    a, b = int(n[0]), int(n[1])
print(a + b)