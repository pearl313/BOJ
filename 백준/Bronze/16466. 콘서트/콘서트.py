import sys
input = sys.stdin.readline

n = int(input())
tickets = set(map(int, input().split()))

i = 1
while True:
    if i in tickets:
        i += 1
    else:
        print(i)
        break