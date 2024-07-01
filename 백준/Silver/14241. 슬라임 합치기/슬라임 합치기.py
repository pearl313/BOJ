import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()), reverse=True)
score = 0
while len(ls) > 1:
    x = ls.pop()
    y = ls.pop()
    score += x * y
    ls.append(x + y)
print(score)