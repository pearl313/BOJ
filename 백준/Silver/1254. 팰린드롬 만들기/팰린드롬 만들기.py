import sys
input = sys.stdin.readline

S = list(input().strip())
i = 1
change = S[:]
while True:
    if change == change[::-1]:
        break
    change = S[:]
    change.extend(S[:i][::-1])
    i += 1
print(len(change))