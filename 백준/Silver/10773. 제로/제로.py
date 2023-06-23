import sys
input = sys.stdin.readline

k = int(input())
ls = []
for _ in range(k):
    n = int(input())
    if n == 0:
        if ls:
            ls.pop()
        else:
            continue
    else:
        ls.append(n)
print(sum(ls))