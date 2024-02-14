import sys
input = sys.stdin.readline

word = list(input().strip())
ans = 0
open = 0
close = 0
total = 0
for i in range(len(word)):
    if word[i] == '(':
        open += 1
        total += 1
    else:
        close += 1
        total -= 1
    if total == 1:
        open = 0
    elif total == -1:
        ans = close
        break
if total == 2:
    ans = open
print(ans)