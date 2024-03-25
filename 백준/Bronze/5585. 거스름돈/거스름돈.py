import sys
input = sys.stdin.readline

pay = int(input())

change = 1000 - pay
money = [500, 100, 50, 10, 5, 1]
total = 0

for i in range(6):
    total += change // money[i]
    change -= (change // money[i]) * money[i]
    
print(total)