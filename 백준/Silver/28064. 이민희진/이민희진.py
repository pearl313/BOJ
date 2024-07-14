import sys
input = sys.stdin.readline

n = int(input())
names = [input().strip() for _ in range(n)]

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        for k in range(1, min(len(names[i]), len(names[j])) + 1):
            if names[i][:k] == names[j][len(names[j]) - k:]:
                cnt += 1
                break
            if names[i][len(names[i]) - k:] == names[j][:k]:
                cnt += 1
                break
print(cnt)