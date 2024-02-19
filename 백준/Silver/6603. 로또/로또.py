import sys
input = sys.stdin.readline

while True:
    ls = list(map(int, input().split()))
    if ls == [0]:
        break
    k = ls[0]
    nums = sorted(ls[1:])
    arr = [0 for _ in range(6)]

    def recur(cur, start):
        if cur == 6:
            print(*arr)
            return
        for i in range(start, k):
            arr[cur] = nums[i]
            recur(cur + 1, i + 1)

    recur(0, 0)
    print()