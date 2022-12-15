button = [0, ' ', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

p, w = map(int, input().split())
message = list(input())
time = 0
for i in range(len(message)):
    for j in range(1, len(button)):
        if i == 0 and message[i] in button[j]:
            time += p * (button[j].index(message[i]) + 1)
            break
        else:
            if message[i] == ' ':
                time += p
                break
            elif message[i] in button[j] and message[i - 1] in button[j]:
                time += w + p * (button[j].index(message[i]) + 1)
                break
            elif message[i] in button[j]:
                time += p * (button[j].index(message[i]) + 1)
                break
print(time)
