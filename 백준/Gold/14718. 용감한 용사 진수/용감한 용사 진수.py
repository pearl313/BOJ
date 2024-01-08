import sys
input = sys.stdin.readline
'''
1. 각 적 병사가 가진 지능을 하나씩 선택하고
2. 모든 병사의 지능을 순회하면서 카운트
3. 카운트가 k 이상되면, 선택한 각 지능 더해서 그 최솟값 구하기
'''
n, k = map(int, input().split())
soldiers = [list(map(int, input().split())) for _ in range(n)]
ans = 1e10
for i in range(n):
    for j in range(n):
        for u in range(n):
            cnt = 0
            for soldier in range(n):
                if soldiers[i][0] >= soldiers[soldier][0] and soldiers[j][1] >= soldiers[soldier][1] and soldiers[u][2] >= soldiers[soldier][2]:
                    cnt += 1
            if cnt >= k:
                ans = min(ans, soldiers[i][0] + soldiers[j][1] + soldiers[u][2])
print(ans)