import sys
input = sys.stdin.readline

def calculate(num, operator):
    global total
    if operator == 0:
        total += num
    elif operator == 1:
        total -= num
    elif operator == 2:
        total *= num
    else:
        if total < 0:
            total = -(-total // num)
        else:
            total //= num


def recur(cur):
    global total, ans_max, ans_min
    if cur == n - 1:
        total = num[0]
        for j in range(1, n):
            calculate(num[j], selected_oper[j - 1])
        ans_max = max(ans_max, total)
        ans_min = min(ans_min, total)
        return
    for i in range(len(oper)):
        if oper[i] != 0:
            selected_oper.append(i)
            oper[i] -= 1
            recur(cur + 1)
            selected_oper.pop()
            oper[i] += 1

n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))

selected_oper = []
total, ans_max, ans_min = 0, -1e10, 1e10
recur(0)
print(ans_max, ans_min, sep='\n')