import sys
input = sys.stdin.readline

k = int(input())
s = input().strip()
pw = ''
for i in range(0, len(s), k):
    pw += s[i]
print(pw)