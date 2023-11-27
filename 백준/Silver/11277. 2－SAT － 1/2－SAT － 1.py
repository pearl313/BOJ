import sys
input = sys.stdin.readline

def recur(cur):
    global ans
    if cur == n:
        x = []
        for j in range(n):
            x.append(True if select[j] else False)
        total = []
        for k in range(m):
            x1, x2 = x[abs(cal[k][0]) - 1], x[abs(cal[k][1]) - 1]
            if cal[k][0] < 0:
                x1 = not x1
            if cal[k][1] < 0:
                x2 = not x2
            if not (x1 or x2):
                return
            total.append(x1 or x2)
        f = total.pop(0)
        while total:
            f = f and total[0]
            total.pop(0)
        if f:
            print(1)
            exit()
        return
    for i in range(2):
        select.append(i)
        recur(cur + 1)
        select.pop()

n, m = map(int, input().split())
cal = [list(map(int, input().split())) for _ in range(m)]
select = []
recur(0)
print(0)