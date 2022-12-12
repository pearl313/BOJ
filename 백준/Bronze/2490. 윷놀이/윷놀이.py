import sys
input = sys.stdin.readline

yut = {0: 'D', 1: 'C', 2: 'B', 3: 'A', 4: 'E'}

for i in range(3):
    ls = list(map(int, input().split()))
    print(yut.get(ls.count(1)))