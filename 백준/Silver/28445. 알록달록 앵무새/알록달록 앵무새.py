import sys
input = sys.stdin.readline

father = sorted(input().split())
mother = sorted(input().split())
possible = sorted(father + mother)
child = set()
for i in range(len(possible)):
    for j in range(len(possible)):
        child.add((possible[i], possible[j]))

for i in sorted(child):
    print(*i)