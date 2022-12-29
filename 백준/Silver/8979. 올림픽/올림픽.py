import sys
input = sys.stdin.readline

N, K = map(int, input().split())
medals = {}
for _ in range(N):
    nation, gold, silver, bronze = map(int, input().split())
    medals[nation] = [gold, silver, bronze]

rank = [0] + sorted(medals.values(), reverse=True)
for i in range(N + 1):
    if rank[i] == medals[K]:
        print(i)
        exit()