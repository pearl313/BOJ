import sys
input = sys.stdin.readline
N, K = map(int, input().split())
S = list(map(int, input().split()))
ans = 0
cnt = 0
tmpK = 0
s, e = 0 , 0
while(e < N):
    if tmpK > K:
        if S[s] % 2 == 0:
            cnt -= 1
        else:
            tmpK -= 1
        s += 1
    elif S[e] % 2 == 0: 
        cnt += 1
        e += 1
    else:
        tmpK += 1
        e += 1
    ans = max(ans,cnt)
print(ans)