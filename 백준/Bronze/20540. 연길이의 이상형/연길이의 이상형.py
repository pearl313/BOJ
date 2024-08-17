import sys
input = sys.stdin.readline

mbti = {'E':'I', 'I':'E', 'S':'N', 'N':'S', 'T':'F', 'F':'T', 'J':'P', 'P':'J'}
s = input().strip()
ans = ''
for i in s:
    ans += mbti[i]
print(ans)