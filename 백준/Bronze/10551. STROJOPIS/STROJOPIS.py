import sys
input = sys.stdin.readline

fingers = ['1QAZ', '2WSX', '3EDC', '4RFV5TGB', '6YHN7UJM', '8IK,', '9OL.', '0P;/-=[]\'']

ans = [0 for _ in range(8)]
for i in input().strip():
    for j in range(len(fingers)):
        if i in fingers[j]:
            ans[j] += 1
for i in ans:
    print(i)