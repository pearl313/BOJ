while True:
    try:
        words = input()
        ls = [0] * 4
        for i in words:
            if i.islower():
                ls[0] += 1
            elif i.isupper():
                ls[1] += 1
            elif i.isdigit():
                ls[2] += 1
            else:
                ls[3] += 1
        print(*ls)
    except EOFError:
        break