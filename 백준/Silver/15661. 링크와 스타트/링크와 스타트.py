import sys
input = sys.stdin.readline

def recur(cur, start, person):
    global ans
    if cur == person:
        link_team = list(set(people) - set(start_team))
        ans = min(ans, abs(cal(start_team) - cal(link_team)))
        return
    for i in range(start, n):
        start_team.append(i)
        recur(cur + 1, i + 1, person)
        start_team.pop()

def cal(ls):
    score = 0
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i == j:
                continue
            score += arr[ls[i]][ls[j]]
    return score

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
people = list(range(n))
start_team = []
link_team = []
ans = 1e10
for i in range(1, n // 2 + 1):
    recur(0, 0, i)
print(ans)