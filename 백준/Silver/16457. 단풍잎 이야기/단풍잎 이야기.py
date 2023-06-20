import sys
input = sys.stdin.readline

def recur(cur, cnt):
    global ans, selected, temp
    if cur == n * 2 + 1:
        if cnt == n:
            temp = 0
            for i in range(m):
                temp_temp = 0
                for j in range(k):
                    if skills[i][j] in selected_key:
                        temp_temp += 1
                if temp_temp == k:
                    temp += 1
            ans = max(ans, temp)
            return
    else:
        selected_key.append(cur)
        recur(cur + 1, cnt + 1)
        selected_key.pop()
        recur(cur + 1, cnt)

n, m, k = map(int, input().split())
skills = [list(map(int, input().split())) for _ in range(m)]
selected_key = []
ans, temp = 0, 0
recur(1, 0)
print(ans)