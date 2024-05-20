ls = list(map(int, input().split()))
if sum(ls) >= 100:
    print('OK')
else:
    temp = ls.index(min(ls))
    if temp == 0:
        print('Soongsil')
    elif temp == 1:
        print('Korea')
    else:
        print('Hanyang')