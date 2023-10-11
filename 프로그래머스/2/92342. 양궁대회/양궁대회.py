def recur(cur, start, n, info):
    global ans, answer
    if cur == n:
        apeach, lion = 0, 0
        for j in range(11):
            if info[10 - j] == selected[j] == 0:
                continue
            elif info[10 - j] >= selected[j]:
                apeach += j
            else:
                lion += j
        if apeach == 17 and lion == 23:
            print('==>', apeach, lion, selected)
        if apeach >= lion:
            return
        elif lion - apeach > ans:
            ans = lion - apeach 
            print(*selected, '->', ans, apeach, lion)
            answer = selected[::-1]
        return
    for i in range(start, 11):
        selected[i] += 1
        recur(cur + 1, i, n, info)
        selected[i] -= 1

selected = [0] * 11
ans = 0
answer = []

def solution(n, info):
    global answer

    recur(0, 0, n, info)
    if ans == 0:
        answer.append(-1)
    # else:
        # answer = selected[::-1]
    
    return answer