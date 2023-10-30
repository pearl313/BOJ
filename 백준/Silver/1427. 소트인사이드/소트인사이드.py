import sys
input = sys.stdin.readline

n = list(input().strip())
n = sorted(n, key=lambda x:int(x), reverse=True)
print(''.join(n))