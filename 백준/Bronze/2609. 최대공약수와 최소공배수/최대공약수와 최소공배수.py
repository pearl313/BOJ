import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    return b

def lcm(a, b):
    return a * b // gcd_val

gcd_val = gcd(a, b)
print(gcd_val, lcm(a, b), sep='\n')