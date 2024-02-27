import sys
input = sys.stdin.readline

n = int(input())
minimum = list(map(int, input().split()))
info = [list(map(int, input().split())) for _ in range(n)]

ans = 1e10
ans_ls = []
def recur(cur, choose, protein, fat, carbo, vita, cost):
    global ans, ans_ls
    if cur == n:
        if protein >= minimum[0] and fat >= minimum[1] and carbo >= minimum[2] and vita >= minimum[3]:
            if ans > cost:
                ans = cost
                temp = []
                for i in choose.split(' '):
                    if i == '':
                        continue
                    temp.append(int(i) + 1)
                ans_ls = [temp]
            elif ans == cost:
                temp = []
                for i in choose.split(' '):
                    if i == '':
                        continue
                    temp.append(int(i) + 1)
                ans_ls.append(temp)
        return

    recur(cur + 1, choose + str(cur) + ' ', protein + info[cur][0], fat + info[cur][1], carbo + info[cur][2], vita + info[cur][3], cost + info[cur][4])
    recur(cur + 1, choose, protein, fat, carbo, vita, cost)

recur(0, '', 0, 0, 0, 0, 0)

if ans == 1e10:
    print(-1)
else:
    print(ans)
    print(*sorted(ans_ls)[0])