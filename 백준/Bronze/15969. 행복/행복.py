import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()))
print(ls[-1] - ls[0])