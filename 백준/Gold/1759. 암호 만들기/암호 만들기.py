from itertools import combinations

L, C = map(int, input().split())
letters = sorted(input().split())

for i in combinations(letters, L):
    # print(i) -> 튜플 형태
    vowel, consonant = 0, 0
    for j in i:
        if j in 'aeiou':
            vowel += 1
        else:
            consonant += 1
    if vowel >= 1 and consonant >= 2:
        print(''.join(i))