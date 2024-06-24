import sys, math
input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result_a = math.ceil(a[1] / b[0])
result_b = math.ceil(b[1] / a[0])

if result_a > result_b:
    print('PLAYER A')
elif result_a < result_b:
    print('PLAYER B')
else:
    print('DRAW')