import sys
input = sys.stdin.readline

t = 0
while True:
    t += 1
    first = input().strip()
    second = input().strip()
    if first == 'END' and second == 'END':
        break
    if len(first) != len(second):
        print(f'Case {t}: different')
        continue

    check = dict()
    for i in first:
        if i in check.keys():
            check[i] += 1
        else:
            check[i] = 1

    same = True
    for i in second:
        if i in check.keys():
            check[i] -= 1
            if check[i] < 0:
                same = False
        else:
            same = False

    if not same:
        print(f'Case {t}: different')
        continue

    for k, v in check.items():
        if v > 0:
            print(f'Case {t}: different')
    else:
        print(f'Case {t}: same')