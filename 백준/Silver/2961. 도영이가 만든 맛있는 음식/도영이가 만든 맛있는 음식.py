import sys, itertools
input = sys.stdin.readline

N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]
arr = list(range(N))
n = 1
ans = float('inf')
while n <= N:
    for i in itertools.combinations(arr, n):
        sour = 1
        bitter = 0
        for j in i:
            sour *= ingredients[j][0]
            bitter += ingredients[j][1]
        temp = abs(sour - bitter)
        ans = min(ans, temp)
    n += 1
print(ans)