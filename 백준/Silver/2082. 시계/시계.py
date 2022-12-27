import sys
input = sys.stdin.readline

num = {
    0: ['###', '#.#', '#.#', '#.#', '###'],
    1: ['..#', '..#', '..#', '..#', '..#'],
    2: ['###', '..#', '###', '#..', '###'],
    3: ['###', '..#', '###', '..#', '###'],
    4: ['#.#', '#.#', '###', '..#', '..#'],
    5: ['###', '#..', '###', '..#', '###'],
    6: ['###', '#..', '###', '#.#', '###'],
    7: ['###', '..#', '..#', '..#', '..#'],
    8: ['###', '#.#', '###', '#.#', '###'],
    9: ['###', '#.#', '###', '..#', '###']
}

clock = [input().split() for _ in range(5)]
no = False
time = ''
n = 0
j = 0
while n != 10 and j != 4:
    for i in range(5):
        for k in range(3):
            if clock[i][j][k] == num[n][i][k]:
                continue
            elif clock[i][j][k] == '#':
                no = True
                break
            else:
                continue
        if no:
            n += 1
            break
    if not no:
        time += str(n)
        n = 0
        j += 1
    if len(time) == 4:
        print(f'{time[:2]}:{time[2:]}')
        exit()
    no = False