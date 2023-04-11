selected = []
sale = [10, 20, 30, 40]
u = []
m = 0
e = []
result = []
answer = []
def nPm(k):
    global selected, m, u, e, result
    if k == m:        
        buy = 0
        plus = 0
        for i in u:
            temp = 0
            for j in range(m):
                if i[0] <= selected[j]:
                    temp += e[j] * (1 - selected[j] * 0.01)
                else:
                    continue
            if temp >= i[1]:
                plus += 1
            else:
                buy += temp
        result.append([plus, buy])
        return
    for i in range(4):
        selected.append(sale[i])
        nPm(k + 1)
        selected.pop()

def solution(users, emoticons):
    global selected, m, u, e, result
    u = users
    m = len(emoticons)
    e = emoticons
    nPm(0)
    return sorted(result, reverse=True)[0]