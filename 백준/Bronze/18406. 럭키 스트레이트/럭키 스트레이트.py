import sys
input = sys.stdin.readline

n = input().strip()
a = n[:len(n) // 2]
b = n[len(n) // 2:]
total_a, total_b = 0, 0
for i in range(len(n) // 2):
    total_a += int(a[i])
    total_b += int(b[i])
print('LUCKY' if total_a == total_b else 'READY')