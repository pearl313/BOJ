import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    one = list(input().split())
    two = list(input().split())
    pwd = list(input().split())

    change = []
    for i in range(n):
        change.append(two.index(one[i]))

    ans = []
    for i in range(n):
        ans.append(pwd[change[i]])
    print(*ans)