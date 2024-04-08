import sys
input = sys.stdin.readline

ls = [input().strip() for _ in range(6)]

word = dict()
for i in ls:
    if not i in word.keys():
        word[i] = 1
    else:
        word[i] += 1


def check(arr):
    check_word = word.copy()
    for i in range(3):
        if not arr[i] in check_word.keys():
            return False
        check_word[arr[i]] -= 1
        if check_word[arr[i]] < 0:
            return False

        temp = ''
        for j in range(3):
            temp += arr[j][i]
        if not temp in check_word.keys():
            return False
        check_word[temp] -= 1
        if check_word[temp] < 0:
            return False

    if sum(check_word.values()) > 0:
        return False

    return True


def recur(cur):
    global ans
    if cur == 3:
        temp = [ls[selected[0]], ls[selected[1]], ls[selected[2]]]
        if check(temp):
            print(*temp, sep='\n')
            exit()
        return
    for i in range(6):
        if visited[i]:
            continue
        selected.append(i)
        visited[i] = True
        recur(cur + 1)
        selected.pop()
        visited[i] = False


selected = []
visited = [False] * 6
recur(0)
print(0)