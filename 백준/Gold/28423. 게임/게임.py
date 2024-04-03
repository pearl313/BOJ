import sys
input = sys.stdin.readline

l, r = map(int, input().split())

def plus(n):
    return sum([int(i) for i in str(n)])

def multi(n):
    total = 1
    for i in str(n):
        total *= int(i)
    return total

def dfs(n):
    if n > 100000:
        return -1

    visited.append(n)
    a = str(plus(n))
    b = str(multi(n))

    num = int(a + b)
    if num == n:
        return 1
    if num in visited:
        return 0
    
    return dfs(num)


ans = 0
for i in range(l, r + 1):
    visited = []
    ans += dfs(i)

print(ans)