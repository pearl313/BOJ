import sys
input = sys.stdin.readline

word = input().strip()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
idx = 0
n = 2
cnt = 0
while idx < len(word):
    temp = word[idx:idx + n]
    if temp in alphabet:
        cnt += 1
        idx += n
        n = 2
    elif n == 3:
        cnt += 1
        idx += 1
        n = 2
    else:
        n += 1
print(cnt)