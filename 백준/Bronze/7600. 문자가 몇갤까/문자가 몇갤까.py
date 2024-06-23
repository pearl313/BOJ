import sys
input = sys.stdin.readline

while True:
    s = input().strip()

    if s == '#':
        break

    ls = dict()
    for i in s:
        if i.isalpha():
            ls[i.lower()] = 1
    print(sum(ls.values()))