import sys
input = sys.stdin.readline

dough_ok = [8, 8, 4, 1, 9]
topping_ok = [1, 30, 25, 10]
one_dough = []
for i in dough_ok:
    one_dough.append(i / 16)
    
T = int(input())
for _ in range(T):
    blank = input().strip()
    dough = list(map(int, input().split()))
    topping = list(map(int, input().split()))
    temp = []
    for i in range(5):
        temp.append(dough[i] // one_dough[i])
    possible = min(temp)
    temp = []
    for j in range(4):
        temp.append(topping[j] // topping_ok[j])
    possible = min(int(possible), sum(temp))
    print(possible)