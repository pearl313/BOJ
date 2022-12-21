import sys
input = sys.stdin.readline

num = '0123456789'
def same(x):
    val = 0
    for i in x:
        if i in num:
            val += int(i)
    return val

N = int(input())
serial_numbers = list(input().strip() for _ in range(N))
serial_numbers.sort(key=lambda x: (len(x), same(x), x))

for i in serial_numbers:
    print(i)