import sys
input = sys.stdin.readline

word = input().strip()
n = int(input())
ring = list(input().strip() for _ in range(n))

cnt = 0
for i in range(n):
    temp = ring[i] + ring[i]
    check = False
    for j in range(len(temp) - len(word) + 1):
        if temp[j:j + len(word)] == word:
            check = True
            break
    if check:
        cnt += 1
print(cnt)