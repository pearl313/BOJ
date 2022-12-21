import sys
input = sys.stdin.readline

dice = [0, 'Yakk', 'Doh', 'Seh', 'Ghar', 'Bang', 'Sheesh']
same = [0, 'Habb Yakk', 'Dobara', 'Dousa', 'Dorgy', 'Dabash', 'Dosh']

T = int(input())
for t in range(1, T + 1):
    a, b = sorted(map(int, input().split()), reverse=True)
    if a == b:
        ans = same[a]
    else:
        ans = dice[a] + ' ' + dice[b]
        if ans == 'Sheesh Bang':
            ans = 'Sheesh Beesh'
    print(f'Case {t}: {ans}')