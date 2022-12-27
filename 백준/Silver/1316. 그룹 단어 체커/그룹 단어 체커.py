import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
letter = []
no = False
for _ in range(N):
    for i in input().strip():
        if not i in letter:
            letter.append(i)
        else:
            if i == letter[-1]:
                continue
            else:
                no = True
    letter = []
    if no:
        no = False
        continue
    else:
        cnt += 1
print(cnt)