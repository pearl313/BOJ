import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, q = map(int, input().split())
video = [list(map(int, input().split())) for _ in range(n - 1)]
questions = [list(map(int, input().split())) for _ in range(q)]

# 연결된 노드, 가중치 정리
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b, c = video[i][0], video[i][1], video[i][2]
    graph[a].append((b, c))
    graph[b].append((a, c))

# 노드끼리의 usado 정리
usado = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n - 1):
    a, b, c = video[i][0], video[i][1], video[i][2]
    usado[a][b] = c
    usado[b][a] = c

# 그래프 탐색해서 usado 찾기
def dfs(s, v, minV):
    visited[v] = True
    for i, j in graph[v]:
        if not visited[i]:
            # 유사도가 k 보다 작으면 더 이상 진행하지 않아도 됨
            if j < k:
                continue
            usado[s][i] = min(minV,j)
            visited[i] = True
            dfs(s, i,usado[s][i])
            

for k, v in questions:
    visited = [False] * (n + 1)
    dfs(v, v, 1e10)
    usado[v][v] = 0

    cnt = 0
    for i in usado[v]:
        if i >= k:
            cnt += 1
    print(cnt)