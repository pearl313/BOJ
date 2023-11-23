import sys
input = sys.stdin.readline

def recur(cur, start, n):
    if cur == k:
        if ''.join(selected) in ans.keys():
            ans[''.join(selected)] += 1
        else:
            ans[''.join(selected)] = 1
        return
    for i in range(start, len(n)):
        selected.append(n[i])
        recur(cur + 1, i + 1, n)
        selected.pop()

x = input().strip()
y = input().strip()
z = input().strip()
k = int(input())
ans = {}
for i in [x, y, z]:
    selected = []
    visited = [False] * len(i)
    recur(0, 0, i)
answer = []
for k, v in ans.items():
    if v >= 2:
        answer.append(k)
if not answer:
    print(-1)
for i in sorted(answer):
    print(i)