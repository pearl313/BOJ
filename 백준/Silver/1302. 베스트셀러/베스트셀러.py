import sys
input = sys.stdin.readline

n = int(input())
book = dict()
for i in range(n):
    name = input().strip()
    if not name in book.keys():
        book[name] = 1
    else:
        book[name] += 1
print(max(sorted(book), key=book.get))