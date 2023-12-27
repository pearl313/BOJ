import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        temp = a % b
        a = b
        b = temp
    return a

a, b = map(int, input().split())
print(a * b // gcd(a, b))