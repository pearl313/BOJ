import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    vps = input().strip()
    if len(vps) % 2 != 0:
        print("NO")
        continue
    possible = 0
    for i in vps:
        if i == '(':
            possible += 1
        elif i == ')':
            if possible:
                possible -= 1
            else:
                print("NO")
                break
    else:
        print("YES" if not possible else "NO")