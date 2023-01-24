import sys
input = sys.stdin.readline

morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '_': '..--', '.': '---.', ',': '.-.-', '?': '----'
}

T = int(input())
for t in range(1, T + 1):
    message = input().strip()
    code = ''
    numbers = []
    for i in message:
        for j in morse.keys():
            if i == j:
                code += morse.get(j)
                numbers.append(len(morse.get(j)))
    ans = ''
    numbers.reverse()
    num = 0
    for n in range(len(numbers)):
        for k, v in morse.items():
            if code[num:sum(numbers[:n + 1])] == v:
                ans += k
                num += numbers[n]
    print(f'{t}: {ans}')