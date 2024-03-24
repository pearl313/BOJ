import sys
input = sys.stdin.readline

l = int(input())
word = input().strip()

ans = 0
for i in range(l):
    ans += (ord(word[i]) - ord('a') + 1) * 31 ** i
print(ans % 1234567891)