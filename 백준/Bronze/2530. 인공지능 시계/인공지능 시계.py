import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
D = int(input())
sec = (C + D) % 60
min = (B + (C + D) // 60) % 60
hour = (A + (B + (C + D) // 60) // 60) % 24
print(hour, min, sec)