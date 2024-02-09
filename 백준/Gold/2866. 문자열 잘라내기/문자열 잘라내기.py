import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = list(input().strip() for _ in range(r))
check = set()
for i in range(c):
    temp = ''
    for j in range(r):
        temp += arr[j][i]
    check.add(temp)
check = list(check)
cnt = 0
while True:
    new_check = set()
    for i in range(c):
        new_check.add(check[i][1:])
    if len(new_check) == c:
        check = list(new_check)
        cnt += 1
    else:
        break
print(cnt)