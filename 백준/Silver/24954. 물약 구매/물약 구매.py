import sys, itertools
input = sys.stdin.readline

N = int(input())
liquid = [0] + list(map(int, input().split()))
change = liquid[:]
discount = [0]
for _ in range(N):
    num = int(input())
    info = [list(map(int, input().split())) for _ in range(num)]
    discount.append(info)
# print(liquid)
# print(discount)
arr = list(range(N + 1))[1:]
# print(arr)
ans = float('inf')
for i in itertools.permutations(arr, N):
    # print(i)
    coin = 0
    for j in i:
        for k in discount[j]:
            # print(k)
            change[k[0]] -= k[1]
            if change[k[0]] <= 0:
                change[k[0]] = 1
        coin += change[j]
        if coin > ans:
            break
    #     print('*', change)
    # print('--', coin)
    ans = min(ans, coin)
    change = liquid[:]
    # print(liquid)
print(ans)