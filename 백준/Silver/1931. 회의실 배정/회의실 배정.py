import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time.sort(key=lambda x:(x[1], x[0]))
cnt = 1
e = time[0][1]
for i in range(1, n):
    if time[i][0] < e:
        continue
    cnt += 1
    e = time[i][1]
    
print(cnt)