import sys
input = sys.stdin.readline

def recur(cur, start):
    if cur == 6:
        print(*selected)
    for i in range(start, len(s)):
        selected.append(s[i])
        recur(cur + 1, i + 1)
        selected.pop()

while True:
    test_case = list(map(int, input().split()))
    if test_case == [0]:
        exit()
    else:
        k = test_case[0]
        s = test_case[1:]
        selected = []
        recur(0, 0)
    print()