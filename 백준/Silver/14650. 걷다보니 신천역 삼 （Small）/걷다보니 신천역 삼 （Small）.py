import sys
input = sys.stdin.readline

def recur(cur):
    global ans
    if cur == n:
        if selected[0] == '0':
            return
        if int(''.join(selected)) % 3 != 0:
            return
        ans += 1
        return
    for i in range(3):
        selected.append(str(i))
        recur(cur + 1)
        selected.pop()

n = int(input())
selected = []
ans = 0
recur(0)
print(ans)