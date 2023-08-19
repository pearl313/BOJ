import sys
input = sys.stdin.readline

s = list(input().strip())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    print(s.count(i), end=' ')