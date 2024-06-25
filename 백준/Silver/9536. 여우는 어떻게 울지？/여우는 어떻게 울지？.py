import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    sound = list(input().split())
    while True:
        animal = list(input().split())

        if animal[-1] == 'say?':
            print(*sound)
            break

        while animal[-1] in sound:
            sound.remove(animal[-1])