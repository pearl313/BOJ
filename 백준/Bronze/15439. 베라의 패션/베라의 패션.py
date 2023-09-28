import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
print(len(list(permutations(list(range(1, n + 1)), 2))))