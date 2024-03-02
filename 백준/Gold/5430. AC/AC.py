import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    ls = input().strip()
    ls = deque(ls[1:len(ls) - 1].split(','))

    new_ls = deque()
    for i in ls:
        if i.isdigit():
            new_ls.append(int(i))

    cnt = 0
    check = False
    for i in p:
        if i == 'R':
            cnt += 1
        else:
            if not new_ls:
                print('error')
                check = True
                break
            if cnt % 2:
                new_ls.pop()
            else:
                new_ls.popleft()

    if new_ls:
        ans = '['
        if cnt % 2:
            for i in range(len(new_ls) - 1, -1, -1):
                if i == 0:
                    ans += str(new_ls[i]) + ']'
                else:
                    ans += str(new_ls[i]) + ','
        else:
            for i in range(len(new_ls)):
                if i == len(new_ls) - 1:
                    ans += str(new_ls[i]) + ']'
                else:
                    ans += str(new_ls[i]) + ','
        print(ans)
    else:
        if not check:
            print('[]')