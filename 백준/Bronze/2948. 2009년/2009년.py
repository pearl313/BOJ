import sys
input = sys.stdin.readline

D, M = map(int, input().split())
days = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
print(days[(months[M - 1] + D) % 7])