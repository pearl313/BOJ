import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
card = deque(range(1, n + 1))
while len(card) > 1:
    print(card.popleft(), end=' ')
    card.append(card.popleft())
print(card.pop())