n = int(input())
cnt = 0
for i in range(1, n + 1):
    if i < 10:
        cnt += 1
        continue
    temp = str(i)
    size = int(temp[0]) - int(temp[1])
    for j in range(1, len(temp) - 1):
        if int(temp[j]) - int(temp[j + 1]) != size:
            break
    else:
        cnt += 1
print(cnt)