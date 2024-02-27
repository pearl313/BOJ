import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(m)]
key = []

def recur(cur, cnt):
    global ans
    if cur == 2 * n + 1:
        if cnt == n:
            q = 0
            for i in ls:
                temp = 0
                for j in range(k):
                    if i[j] in key:
                        temp += 1
                if temp == k:
                    q += 1
            ans = max(ans, q)
        return

    key.append(cur)
    recur(cur + 1, cnt + 1)
    key.pop()
    recur(cur + 1, cnt)

ans = -1e10
recur(1, 0)
print(ans)