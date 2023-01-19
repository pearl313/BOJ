import sys, itertools
input = sys.stdin.readline

def dfs(start, ls):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            if i in j or i in unselect:
                ls.append(i)
                dfs(i, ls)

N =int(input())
population = [0] +list(map(int, input().split()))
total = sum(population)
graph = list([0] for _ in range(N + 1))
for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    graph[i] = temp[1:]
visited = [False] * (N + 1)
arr = list(range(1, N + 1))
ans = float('inf')
for i in range(1, N // 2 + 1):
    for j in itertools.combinations(arr, i):
        cnt = 0
        select = [j[0]]
        unselect = []
        dfs(j[0], select)
        if len(select) == len(j):
            unselect = []
            for k in arr:
                if not k in select:
                    unselect.append(k)
            check = [unselect[0]]
            dfs(unselect[0], check)
            if sorted(check) == unselect:
                one = 0
                for k in select:
                    one += population[k]
                two = total - one
                ans = min(ans, abs(one - two))
        visited = [False] * (N + 1)
if ans == float('inf'):
    ans = -1
print(ans)