import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().split()
    if sorted(list(a)) != sorted(list(b)):
        print(f'{a} & {b} are NOT anagrams.')
    else:
        print(f'{a} & {b} are anagrams.')