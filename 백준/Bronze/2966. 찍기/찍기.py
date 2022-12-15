import sys
input = sys.stdin.readline

a = ['A', 'B', 'C']
b = ['B', 'A', 'B', 'C']
g = ['C', 'C', 'A', 'A', 'B', 'B']
n = 3
while n != 101:
    a.append(a[n - 3])
    b.append(b[n - 3])
    g.append(g[n - 3])
    n += 1
Adrian = Bruno = Goran = 0
N = int(input())
ans = input().strip()
for i in range(len(ans)):
    if ans[i] == a[i]:
        Adrian += 1
    if ans[i] == b[i]:
        Bruno += 1
    if ans[i] == g[i]:
        Goran += 1
first = max(Adrian, Bruno, Goran)
answer = []
students = [Adrian, Bruno, Goran]
name = ['Adrian', 'Bruno', 'Goran']
for j in range(3):
    if first == students[j]:
        answer.append(name[j])
print(first)
for k in answer:
    print(k)