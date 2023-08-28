import sys
input = sys.stdin.readline

one = int(input())
two = int(input())
three = int(input())
total = one + two + three
if one == two == three:
    print('Equilateral')
elif total == 180:
    if one == two or two == three or one == three:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')