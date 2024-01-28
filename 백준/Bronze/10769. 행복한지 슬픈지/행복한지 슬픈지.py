import sys
input = sys.stdin.readline

s = input().strip()
happy = s.count(':-)')
sad = s.count(':-(')
if happy or sad:
    if happy > sad:
        print('happy')
    elif sad > happy:
        print('sad')
    else:
        print('unsure')
else:
    print('none')