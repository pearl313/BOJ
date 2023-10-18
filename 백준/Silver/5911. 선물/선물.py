import sys
input = sys.stdin.readline

n, b = map(int, input().split())
present = sorted(list(map(int, input().split())) for _ in range(n))
# print(present)
ans = 0
for i in range(n):
    data = []
    for j in range(n):
        if i == j:
            # print('=>', i)
            data.append(present[i][0] // 2 + present[i][1])
        else:
            data.append(sum(present[j]))


    total = 0
    cnt = 0
    data.sort()
    for j in range(n):
        total += data[j]
        if total > b:
            break
        cnt += 1
    ans = max(ans, cnt)
print(ans)