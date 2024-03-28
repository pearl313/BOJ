import sys
input = sys.stdin.readline

total = 0
ans = -1e10
for _ in range(10):
    get_off, get_on = map(int, input().split())
    total += get_on
    total -= get_off
    ans = max(ans, total)
    
print(ans)