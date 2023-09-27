while True:
    line = sorted(map(int, input().split()))
    if sum(line) == 0:
        break
    if line[2] ** 2 == line[0] ** 2 + line[1] ** 2:
        print('right')
    else:
        print('wrong')