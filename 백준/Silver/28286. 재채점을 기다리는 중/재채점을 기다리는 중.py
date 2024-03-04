import sys
input = sys.stdin.readline

n, k = map(int, input().split())
answer = list(map(int, input().split()))
omr = list(map(int, input().split()))

ans = -1e10

def pull(cur, temp):
    new_temp = temp[:]
    new_temp.pop(cur)
    new_temp.append('.')
    return new_temp

def push(cur, temp):
    new_temp = temp[:]
    new_temp.insert(cur, '.')
    new_temp.pop()
    return new_temp

def recur(cnt, ls):
    global ans
    temp = 0
    for j in range(n):
        if answer[j] == ls[j]:
            temp += 1
    ans = max(ans, temp)

    if cnt >= k:
        return

    for i in range(n):
        recur(cnt + 1, push(i, ls))
        recur(cnt + 1, pull(i, ls))

recur(0, omr)
print(ans)