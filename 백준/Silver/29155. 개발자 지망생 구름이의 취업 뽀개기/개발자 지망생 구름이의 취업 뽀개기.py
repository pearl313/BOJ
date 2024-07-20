import sys
input = sys.stdin.readline

n = int(input())
cnt_ls = [0] + list(map(int, input().split()))
problem_ls = [list(map(int, input().split())) for _ in range(n)]
problem_ls.sort()

time = 0
level = 1
before = 0
for k, t in problem_ls:
    # 해당 난이도에 풀어야하는 문제 수가 남았을 경우,
    if cnt_ls[k] > 0:
        # 첫 문제일 경우,
        if time == 0:
            time += t
        # 난이도가 같은 경우,
        elif level == k:
            time += abs(before - t) + t
        else:
            time += 60 + t
        level = k
        before = t
        cnt_ls[k] -= 1
print(time)