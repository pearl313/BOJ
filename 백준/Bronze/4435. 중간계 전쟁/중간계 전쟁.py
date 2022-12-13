import sys
input = sys.stdin.readline

gan = [1, 2, 3, 3, 4, 10]
sa = [1, 2, 2, 2, 3, 5, 10]

T = int(input())
for t in range(T):
    gan_ls = list(map(int, input().split()))
    sa_ls = list(map(int, input().split()))
    score_gan = 0
    score_sa = 0
    for i in range(len(gan_ls)):
        score_gan += gan_ls[i] * gan[i]
    for j in range(len(sa_ls)):
        score_sa += sa_ls[j] * sa[j]
    if score_gan < score_sa:
        print(f'Battle {t + 1}: Evil eradicates all trace of Good')
    elif score_gan > score_sa:
        print(f'Battle {t + 1}: Good triumphs over Evil')
    else:
        print(f'Battle {t + 1}: No victor on this battle field')