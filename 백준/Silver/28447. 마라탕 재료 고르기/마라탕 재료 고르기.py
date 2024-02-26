import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]

def recur(cur, choose):
    global ans
    if cur == n:
        if len(choose) == k:
            temp = 0
            for i in range(k):
                for j in range(i + 1, k):
                    temp += ls[int(choose[i])][int(choose[j])]
            ans = max(ans, temp)
        return

    recur(cur + 1, choose + str(cur))
    recur(cur + 1, choose)

ans = -1e10
recur(0, '')
print(ans)