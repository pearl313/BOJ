N = int(input())
ls = sorted(map(int, input().split()))
value = 0
for i in range(-1, N - 1):
    value += abs(ls[i] - ls[i + 1])

print(value)