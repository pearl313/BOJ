import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
ls = sorted(str(a * b * c), key=lambda x:int(x))
num = [0] * 10
for i in range(len(ls)):
    num[int(ls[i])] += 1
print(*num, sep='\n')