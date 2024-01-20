import sys
input = sys.stdin.readline
'''
더한 값을 바로 절대값 처리하지 말고,
양수인지 음수인지에 따라서 포인터의 위치 바꿔줌 
'''
n = int(input())
solutions = sorted(map(int, input().split()))
s, e = 0, (n - 1)
ans = 1e10
ans1, ans2 = 0, 0
while s < e:
    temp = solutions[s] + solutions[e]
    if temp == 0:
        ans1 = solutions[s]
        ans2 = solutions[e]
        break
    elif abs(temp) < ans:
        ans = abs(temp)
        ans1 = solutions[s]
        ans2 = solutions[e]
    elif temp > 0:
        e -= 1
    else:
        s += 1
print(ans1, ans2)