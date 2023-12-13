import sys
input = sys.stdin.readline

score = []
for i in range(1, 9):
    score.append([i, int(input().strip())])
score = sorted(sorted(score, key=lambda x:-x[1])[:5])
nums = [i[0] for i in score]
total = [i[1] for i in score]
print(sum(total))
print(*nums)