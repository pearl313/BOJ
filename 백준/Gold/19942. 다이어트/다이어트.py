import sys
input = sys.stdin.readline

def recur(cur, protein, fat, carbo, vita, cost):
    global ans, ans_ls
    if cur == n:
        if protein >= min_val[0] and fat >= min_val[1] and carbo >= min_val[2] and vita >= min_val[3]:
            if cost < ans:
                ans = cost
                ans_ls = [[i + 1 for i in selected]]
            elif cost == ans:
                ans_ls.append([i + 1 for i in selected])
        return
    selected.append(cur)
    recur(cur + 1, protein + ingredients[cur][0], fat + ingredients[cur][1], carbo + ingredients[cur][2],
          vita + ingredients[cur][3], cost + ingredients[cur][4])
    selected.pop()
    recur(cur + 1, protein, fat, carbo, vita, cost)

n = int(input())
min_val = list(map(int, input().split()))
ingredients = [list(map(int, input().split())) for _ in range(n)]
ans = 1e10
ans_ls = []
selected = []
recur(0, 0, 0, 0, 0, 0)
if ans == 1e10:
    print(-1)
else:
    print(ans)
    print(*sorted(ans_ls)[0])