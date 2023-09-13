import sys
input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    word = list(input().split())
    if word[0] == 'push':
        queue.append(int(word[-1]))
    elif word[0] == 'pop':
        if queue == []:
            print(-1)
        else:
            print(queue[0])
            queue.remove(queue[0])
    elif word[0] == 'size':
        print(len(queue))
    elif word[0] == 'empty':
        print(0 if queue else 1)
    elif word[0] == 'front':
        print(queue[0] if queue else -1)
    elif word[0] == 'back':
        print(queue[-1] if queue else -1)