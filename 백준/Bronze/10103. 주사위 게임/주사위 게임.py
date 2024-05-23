import sys
input = sys.stdin.readline

t = int(input())
one, two = 100, 100
for i in range(t):
    a, b = map(int, input().split())
    if a > b:
        two -= a
    elif b > a:
        one -= b
    else:
        continue
print(one, two, sep='\n')