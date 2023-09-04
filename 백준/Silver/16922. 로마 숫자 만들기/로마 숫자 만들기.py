import sys
input = sys.stdin.readline

def recur(cur, start):
    if cur == n:
        nums.add(sum(selected))
        return
    for i in range(start, 4):
        selected.append(word[i])
        recur(cur + 1, i)
        selected.pop()

n = int(input())
word = [1, 5, 10, 50]
nums = set()
selected = []
recur(0, 0)
print(len(nums))