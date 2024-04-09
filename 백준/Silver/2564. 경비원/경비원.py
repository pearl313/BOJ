import sys
input = sys.stdin.readline

width, height = map(int, input().split())
n = int(input())
store = [list(map(int, input().split())) for _ in range(n)]
dongeun = list(map(int, input().split()))

total = 0
for i in range(n):
    d, p = store[i][0], store[i][1]
    
    if d == dongeun[0]:
        total += abs(p - dongeun[1])
        continue
    
    dist = 0
    if d == 1:
        if dongeun[0] == 2:
            dist += height
            dist += min(p + dongeun[1], width * 2 - (p + dongeun[1]))
        elif dongeun[0] == 3:
            dist += p + dongeun[1]
        elif dongeun[0] == 4:
            dist += width - p + dongeun[1]
    elif d == 2:
        if dongeun[0] == 1:
            dist += height
            dist += min(p + dongeun[1], width * 2 - (p + dongeun[1]))
        elif dongeun[0] == 4:
            dist += (height - dongeun[1]) + (width - p)
        elif dongeun[0] == 3:
            dist += height - dongeun[1] + p
    elif d == 3:
        if dongeun[0] == 4:
            dist += width
            dist += min(p + dongeun[1], height * 2 - (p + dongeun[1]))
        elif dongeun[0] == 1:
            dist += p + dongeun[1]
        elif dongeun[0] == 2:
            dist += (height - p) + dongeun[1]
    elif d == 4:
        if dongeun[0] == 3:
            dist += width
            dist += min(p + dongeun[1], height * 2 - (p + dongeun[1]))
        elif dongeun[0] == 2:
            dist += (height - p) + (width - dongeun[1])
        elif dongeun[0] == 1:
            dist += (width - dongeun[1]) + p
            
    total += dist
    
print(total)