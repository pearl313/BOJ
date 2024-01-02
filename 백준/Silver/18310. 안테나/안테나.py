import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()))
print(ls[len(ls) // 2] if len(ls) % 2 else ls[len(ls) // 2 - 1])