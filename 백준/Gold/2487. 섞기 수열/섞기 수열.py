import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
ls = [0] + list(map(int, input().split()))

# 최대공약수
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소공배수
def get_lcm(a, b):
    return a // get_gcd(a, b) * b

# 그룹 찾기
def find_cnt(number, i):
    global group, check

    check[number] = 1

    if ls[number] == i:
        return

    group[i].append(ls[number])
    find_cnt(ls[number], i)


# 숫자 확인하는 배열
check = [0] * (n + 1)
group = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    if check[i]:
        continue
    group[i].append(i)
    find_cnt(i, i)

len_ls = []
# 개수 세어주기
for i in group:
    if not i:
        continue
    len_ls.append(len(i))

# 최소공배수 찾기
ans = 1
for i in range(len(len_ls)):
    ans = get_lcm(ans, len_ls[i])
print(ans)