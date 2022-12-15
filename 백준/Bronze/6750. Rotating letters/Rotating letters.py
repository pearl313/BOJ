import sys
input = sys.stdin.readline

letters = 'IOSHZXN'
ans = 'YES'
for i in input().strip():
    if not i in letters:
        ans = 'NO'
        break
print(ans)