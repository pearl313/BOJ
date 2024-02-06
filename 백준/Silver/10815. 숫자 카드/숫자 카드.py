N = int(input())
S_card = set(map(int, input().split()))
M = int(input())
check = set(map(int, input().split()))
ans = []
for i in check:
    if i in S_card:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)