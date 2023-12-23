import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def gcd_n(arr):
    num = arr[0]
    for i in arr:
        num = gcd(num, i)
    return num

n = int(input())
ls = [int(input()) for _ in range(n)]
dist = set()
for i in range(1, n):
    dist.add(ls[i] - ls[i - 1])
    
j = gcd_n(list(dist))
i = 0
start = ls[i]
cnt = 0
while start < ls[-1]:
    if start + j == ls[i + 1]:
        i += 1
    else:
        cnt += 1
    start += j
print(cnt)

