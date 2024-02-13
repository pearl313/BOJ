word = input()
vowel = 'aeiou'
cnt = 0
for i in word:
    if i in vowel:
        cnt += 1
print(cnt)