import sys
input = sys.stdin.readline

ls = list(range(1, 31))
for _ in range(28):
    ls.remove(int(input()))
for i in ls:
    print(i)