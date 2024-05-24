alpha = dict()
while True:
    try:
        sentence = input()
        for i in sentence:
            if i == ' ':
                continue
            elif i in alpha.keys():
                alpha[i] += 1
            else:
                alpha[i] = 1
    except EOFError:
        print(''.join(sorted([k for k, v in alpha.items() if max(alpha.values()) == v])))
        exit()