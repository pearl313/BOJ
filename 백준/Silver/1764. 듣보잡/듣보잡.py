import sys
input = sys.stdin.readline

n, m = map(int, input().split())
names = {}
ans = []
for i in range(n + m):
    name = input().strip()
    if not name in names.keys():
        names[name] = 1
    else:
        ans.append(name)
print(len(ans))
for a in sorted(ans):
    print(a)