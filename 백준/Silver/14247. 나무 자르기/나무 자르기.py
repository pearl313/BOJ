import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
height = list(map(int, input().split()))

ls = [[] for _ in range(n)]
for i in range(n):
    ls[i] = [height[i], tree[i]]
    
ls.sort()
total = 0
for i in range(n):
    total += ls[i][1] + (ls[i][0] * i)
print(total)