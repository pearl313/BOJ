import sys
input = sys.stdin.readline

'''
1. 가장 큰 기둥을 찾아야 함
2. 가장 큰 기둥을 만나기 전까지는 한 칸씩 이동하면서 높이 갱신
3. 뒤에서부터 큰 기둥을 만나기 전까지 높이 갱신 진행
4. 그 값을 다 더해줌
'''

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
ls.sort(key=lambda x:x[0])
max_ls = max(ls, key=lambda x:x[1])
height = ls[0][1]
area = max_ls[1]
# 앞에서부터 큰 기둥까지
for i in range(1, ls.index(max_ls) + 1):
    area += height * (ls[i][0] - ls[i - 1][0])
    if height > ls[i][1]:
        continue
    height = ls[i][1]
height = ls[-1][1]
# 뒤에서부터 큰 기둥까지
for i in range(n - 2, ls.index(max_ls) - 1, -1):
    area += height * (ls[i + 1][0] - ls[i][0])
    if height > ls[i][1]:
        continue
    height = ls[i][1]
print(area)