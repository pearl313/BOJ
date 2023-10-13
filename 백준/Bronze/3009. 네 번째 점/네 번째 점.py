import sys
input = sys.stdin.readline

dot_x = []
dot_y = []
for _ in range(3):
    x, y = map(int, input().split())
    dot_x.append(x)
    dot_y.append(y)

for i in range(3):
    if dot_x.count(dot_x[i]) == 1:
        x4 = dot_x[i]
    if dot_y.count(dot_y[i]) == 1:
        y4 = dot_y[i]
print(x4, y4)