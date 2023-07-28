import sys
input = sys.stdin.readline

n = int(input())
# 제곱수는 1로 저장하고 나머지는 0으로 저장
arr = [0 if i ** 0.5 % 1 else 1 for i in range(n + 1)]
# 4 혹은 그 이하의 개수로 찾아야 함
ans = 4
for i in range(int(n ** 0.5), 0, -1):
    # n이 제곱수일 경우, 하나로 제곱을 나타낼 수 있음
    if arr[n]:
        ans = 1
        break
    # n에서 제곱수 i를 뺀 나머지가 제곱수일 경우 -> 2개로 나타낼 수 있음 
    elif arr[n - i ** 2]:
        ans = 2
        break
    else:
        # n에서 제곱수 i를 뺀 상태에서 다시 한번 더 j의 제곱을 뺏을 때 제곱수일 경우 -> 3개로 나타낼 수 있음 
        for j in range(int((n - i ** 2) ** 0.5), 0, -1):
            if arr[(n - i ** 2) - j ** 2]:
                ans = 3
print(ans)