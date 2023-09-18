import sys
input = sys.stdin.readline

ls = list(int(input()) for _ in range(9))
print(max(ls), ls.index(max(ls)) + 1, sep='\n')