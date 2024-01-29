import sys
input = sys.stdin.readline

h, w = map(int, input().split())
ls = [0] + list(map(int, input().split()))
max_idx = ls.index(max(ls))

new_ls = ls[::]
for i in range(1, max_idx + 1):
    new_ls[i] = new_ls[i] if new_ls[i] > new_ls[i - 1] else new_ls[i - 1]
for i in range(w - 1, max_idx, -1):
    new_ls[i] = new_ls[i] if new_ls[i] > new_ls[i + 1] else new_ls[i + 1]
ans = 0
for i in range(1, w + 1):
    if new_ls[i] > ls[i]:
        ans += new_ls[i] - ls[i]
print(ans)