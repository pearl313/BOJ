n = int(input())
cute = 0
for _ in range(n):
    if int(input()) == 1:
        cute += 1
print('Junhee is not cute!' if (n - cute) > cute else 'Junhee is cute!')