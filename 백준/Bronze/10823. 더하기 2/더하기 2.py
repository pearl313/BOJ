s = ''
while True:
    try:
        s += input()
    except EOFError:
        break

print(sum(list(map(int, s.split(',')))))