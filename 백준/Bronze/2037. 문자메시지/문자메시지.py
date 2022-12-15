button = [0, ' ', '와ABC', '와DEF', '와GHI', '와JKL', '와MNO', '와PQRS', '와TUV', '와WXYZ']

p, w = map(int, input().split())
message = input()
time = 0

for i in range(len(message)):
    for j in range(1, len(button)):
        if i == 0 and message[i] in button[j]:
            time += p * (button[j].index(message[i]))
            break
        else:
            if message[i] == ' ':
                time += p
                break
            elif message[i] in button[j] and message[i - 1] in button[j]:
                time += p * (button[j].index(message[i])) + w
                break
            elif message[i] in button[j]:
                time += p * (button[j].index(message[i]))
                break
print(time)