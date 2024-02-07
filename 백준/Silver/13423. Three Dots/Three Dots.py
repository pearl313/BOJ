import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    ls = sorted(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist = (ls[i] + ls[j]) / 2
            s, e = i, j
            while s <= e:
                mid = (s + e) // 2
                if ls[mid] == dist:
                    cnt += 1
                    break
                elif ls[mid] < dist:
                    s = mid + 1
                else:
                    e = mid - 1
    print(cnt)