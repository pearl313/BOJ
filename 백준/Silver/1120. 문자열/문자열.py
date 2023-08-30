import sys
input = sys.stdin.readline

a, b = input().split()
ans = 1e10
# b랑 a랑 길이를 같게 맞추기
for i in range(len(b) - len(a) + 1):
    # a랑 b랑 같은 길이로 비교했을 때 다른 알파벳 개수
    cnt = 0
    # a의 길이에 맞춰서 비교해주기
    for j in range(len(a)):
        if a[j] != b[i + j]:
            cnt += 1
    ans = min(ans, cnt)
print(ans)