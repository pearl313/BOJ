import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(range(N + 1))[1:]
ans = []
i = K
ans.append(arr[i - 1])
arr[i - 1] = 0
while arr != [0] * N:
    cnt = 0
    while cnt < K:
        i += 1
        i %= N
        if arr[i - 1]:
            cnt += 1
    # i = (i + K) % N
    ans.append(arr[i - 1])
    arr[i - 1]= 0
# print(ans)
print('<', end='')
for i in ans:
    if i == ans[-1]:
        print(i, end='')
    else:
        print(i, end=', ')

print('>')