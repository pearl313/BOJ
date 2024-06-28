import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
total = sum(time) + (len(time) - 1) * 8
print(total // 24, total % 24)