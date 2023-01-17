import sys
input = sys.stdin.readline

character = {' ': '%20', '!': '%21', '$': '%24', '%': '%25', '(': '%28', ')': '%29', '*': '%2a'}

while True:
    message = input().strip()
    if message == '#':
        break
    ans = ''
    for i in message:
        if i in character.keys():
            ans += character.get(i)
        else:
            ans += i
    print(ans)