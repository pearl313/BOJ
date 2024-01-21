import sys
input = sys.stdin.readline
'''
소수 리스트 먼저 만들고 가능한 경우의 수 찾기 
'''
n = int(input())
ls = []
isPrime = [True for _ in range(n + 1)]
isPrime[1] = False
for i in range(2, n + 1):
    if not isPrime[i]:
        continue
    for j in range(i * i, n + 1, i):
        isPrime[j] = False
    ls.append(i)

s, e = 0, 0
temp = sum(ls[s:e + 1])
cnt = 0
while e < len(ls):
    if temp == n:
        cnt += 1
        temp -= ls[s]
        s += 1
        e += 1
        if e == len(ls):
            break
        temp += ls[e]
    elif temp > n:
        temp -= ls[s]
        s += 1
    else:
        e += 1
        if e == len(ls):
            break
        temp += ls[e]
print(cnt)