import sys
input = sys.stdin.readline

num_1 = list(input().strip())
num_2 = list(input().strip())
num_1, num_2 = num_1[::-1], num_2[::-1]
ans = 0
for i in range(len(num_2)):
    temp = 0
    for j in range(len(num_1)):
        temp += int(str(int(num_2[i]) * int(num_1[j])) + '0' * j)
    print(temp)
    ans += int(str(temp) + '0' * i)
print(ans)