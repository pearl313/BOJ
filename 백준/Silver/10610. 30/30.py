import sys
input = sys.stdin.readline

n = list(input().strip())
total = 0
ans = 0
for i in n:
    total += int(i)
if total % 3 == 0 and '0' in n:
    n = sorted(n, key=lambda x:int(x), reverse=True)
    print(''.join(n))
else:
    print(-1)