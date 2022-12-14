import sys
input = sys.stdin.readline

end_nums = [0, 666]
n = 1
i = 667
while n != 10001:
    if '666' in str(i):
        end_nums.append(i)
        n += 1
    i += 1
print(end_nums[int(input())])