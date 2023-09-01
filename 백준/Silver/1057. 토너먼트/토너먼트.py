import sys
input = sys.stdin.readline

n, jimin, hansoo = map(int, input().split())
cnt = 0
while jimin != hansoo:
    jimin -= jimin // 2
    hansoo -= hansoo // 2
    cnt += 1
print(cnt)