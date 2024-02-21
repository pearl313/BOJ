def is_good_sequence(s):
    length = len(s)
    for i in range(1, length // 2 + 1):
        if s[-i:] == s[-2*i:-i]:
            return False
    return True

def recur(cur, arr):
    if not is_good_sequence(arr):
        return None
    if cur == n:
        return arr
    for i in range(1, 4):
        result = recur(cur + 1, arr + [i])
        if result:
            return result

n = int(input())
ans = recur(0, [])

print(''.join(map(str, ans)))