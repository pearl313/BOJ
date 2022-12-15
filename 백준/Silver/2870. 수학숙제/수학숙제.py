# 114328 KB / 116 ms
# 입력받은 단어의 각 문자를 확인해보기!

import sys
input = sys.stdin.readline

M = int(input())
ans = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
num = ''                                             # 각 숫자들을 합쳐주기 위해서 문자열 사용
for i in range(M):
    word = input().strip()
    for j in range(len(word)):
        if not word[j] in alphabet:
            num += word[j]                           # num에 숫자 이어 붙여서 임시 저장
        elif word[j] in alphabet:
            if len(num) == 0:                        # 저장된 숫자 없으면 다음으로 넘어가기
                continue
            ans.append(int(num))                     # 리스트에 임시 저장했던 숫자를 정수로 넣기 -> 앞에 있는 0 사라짐 
            num = ''                                 # 초기화
        if j == len(word) - 1 and len(num) != 0:     # 단어의 맨 마지막 문자이고, 저장된 숫자가 있다면,
            ans.append(int(num))                     # 리스트에 정수로 저장
            num = ''                                 # 초기화
for n in sorted(ans):
    print(n)