import sys
input = sys.stdin.readline

n = int(input())
ls = list(input().split())
arr = [0 for _ in range(n + 1)]
visited = [False for _ in range(10)]

def check(cur):
    if cur <= 1:
        return True
    if ls[cur - 2] == '<' and arr[cur - 2] > arr[cur - 1]:
        return False
    if ls[cur - 2] == '>' and arr[cur - 2] < arr[cur - 1]:
        return False
    return True

def recur(cur):
    # 가지치기
    if not check(cur):
        return
    # 기저 조건
    if cur == n + 1:
        ans.append(arr[:])
        return
    # 재귀 호출
    for i in range(10):
        if visited[i]:
            continue
        visited[i] = True
        arr[cur] = i
        recur(cur + 1)
        visited[i] = False
ans = []
recur(0)
print(''.join(map(str, ans[-1])))
print(''.join(map(str, ans[0])))