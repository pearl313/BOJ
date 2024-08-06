import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ls = [0]
i = 1
while True:
    for j in range(i):
        ls.append(i)
    i += 1
    if len(ls) > b:
        break
        
ans = 0
for i in range(a, b + 1):
    ans += ls[i]
print(ans)