import sys
input = sys.stdin.readline

n = int(input())
ls = [list(input().split()) for _ in range(n)]

# 바로 앞 전에 이긴 팀과 시간
win = [0, 0]
# 각 팀의 스코어랑 이긴 시간
team1 = [0, 0]
team2 = [0, 0]
for score, time in ls:
    if score == '1':
        team1[0] += 1
    else:
        team2[0] += 1

    min, sec = map(int, time.split(':'))
    time = min * 60 + sec
    if team1[0] > team2[0]:
        if win[0] == 0:
            win[0] = 1
            win[1] = time
    elif team1[0] < team2[0]:
        if win[0] == 0:
            win[0] = 2
            win[1] = time
    else:
        if win[0] == 1:
            team1[1] += time - win[1]
        else:
            team2[1] += time - win[1]
        win[0] = 0

# 다 끝나고 마지막
if win[0] == 1:
    team1[1] += 48 * 60 - win[1]
elif win[0] == 2:
    team2[1] += 48 * 60 - win[1]

print((('0' + str(team1[1] // 60)) if len(str(team1[1] // 60)) == 1 else str(team1[1] // 60)) + ':' + (('0' + str(team1[1] % 60)) if len(str(team1[1] % 60)) == 1 else str(team1[1] % 60)))
print((('0' + str(team2[1] // 60)) if len(str(team2[1] // 60)) == 1 else str(team2[1] // 60)) + ':' + (('0' + str(team2[1] % 60)) if len(str(team2[1] % 60)) == 1 else str(team2[1] % 60)))