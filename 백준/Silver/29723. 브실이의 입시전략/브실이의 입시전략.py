import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ls = dict()
for _ in range(n):
    name, score = input().split()
    ls[name] = int(score)

must = 0
for _ in range(k):
    lecture = input().strip()
    must += ls[lecture]
    ls.pop(lecture)

ls = sorted(ls.items(), key=lambda x:x[1])
min_val, max_val = 0, 0
for i in range(m - k):
    min_val += ls[i][1]
    max_val += ls[-i - 1][1]
print(must + min_val, must + max_val)