import sys
input = sys.stdin.readline

n, s, r = map(int, input().split())
broken = sorted(map(int, input().split()))
one_more = sorted(map(int, input().split()))
check = [0] * (n + 1)

for i in range(1, n + 1):
    if i in broken:
        check[i] += 1
    if i in one_more:
        check[i] += 1
    if check[i] == 2:
        broken.remove(i)
        one_more.remove(i)

ans = 0
for i in range(len(broken)):
    if broken[i] - 1 in one_more:
        one_more.remove(broken[i] - 1)
    elif broken[i] + 1 in one_more:
        one_more.remove(broken[i] + 1)
    else:
        ans += 1

print(ans)