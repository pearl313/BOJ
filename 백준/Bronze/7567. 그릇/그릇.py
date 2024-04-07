import sys
input = sys.stdin.readline

s = input().strip()

height = 10
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        height += 10
    else:
        height += 5

print(height)