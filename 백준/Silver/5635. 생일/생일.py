import sys
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    name, *info = input().split()
    for i in range(3):
        info[i] = int(info[i])
    ls.append([name, info])
ls.sort(key=lambda x:(x[1][-1], x[1][-2]))
print(ls[-1][0], ls[0][0], sep='\n')