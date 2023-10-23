import sys
input = sys.stdin.readline

x, y = map(int, input().split())
year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(day[(sum(year[:x]) + y) % 7])