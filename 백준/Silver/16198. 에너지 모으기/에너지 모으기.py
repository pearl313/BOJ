import sys
input = sys.stdin.readline

def recur(cur):
    global ans
    if cur == n - 2:
        energy = 0
        possible = beads[:]
        for j in selected:
            forward = j - 1
            back = j + 1
            while possible[forward] == 0 or possible[back] == 0:
                if possible[forward] == 0:
                    forward -= 1
                if possible[back] == 0:
                    back += 1
            energy += possible[forward] * possible[back]
            possible[j] = 0
        ans = max(ans, energy)
        return
    for i in range(1, n - 1):
        if not visited[i]:
            selected.append(i)
            visited[i] = True
            recur(cur + 1)
            selected.pop()
            visited[i] = False

n = int(input())
beads = list(map(int, input().split()))
selected = []
visited = [False] * n
ans = 0
recur(0)
print(ans)