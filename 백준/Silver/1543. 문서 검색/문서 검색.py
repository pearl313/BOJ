import sys
input = sys.stdin.readline

text = list(input().strip())
word = list(input().strip())
cnt = 0
n = 0
while n <= len(text) - len(word):
    if text[n:n + len(word)] == word:
        cnt += 1
        n += len(word)
    else:
        n += 1
print(cnt)