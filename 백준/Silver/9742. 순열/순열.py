import sys
input = sys.stdin.readline

def recur(cur):
    global cnt, ans
    if cur == len(a):
        cnt += 1
        if cnt == b:
            print(''.join(a), b, '=', ''.join(selected))
            ans = True
        return
    for i in range(len(a)):
        if not visited[i]:
            selected.append(a[i])
            visited[i] = True
            recur(cur + 1)
            selected.pop()
            visited[i] = False

while True:
    try:
        a, b = input().split()
        a = sorted(a)
        b = int(b)
        selected = []
        visited = [False] * (len(a) + 1)
        cnt = 0
        ans = False
        recur(0)
        if not ans:
            print(''.join(a), b, '=', 'No permutation')
    except:
        break