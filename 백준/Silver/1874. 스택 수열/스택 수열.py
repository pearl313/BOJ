import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        cur += 1
        ans.append('+')
    if stack[-1] == num:
        ans.append('-')
        stack.pop()
    else:
        print("NO")
        exit()
for i in ans:
    print(i)