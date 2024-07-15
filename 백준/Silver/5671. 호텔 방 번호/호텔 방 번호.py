import sys
input = sys.stdin.readline

while True:
    try:
        n, m = map(int, input().split())
        cnt = 0
        for i in range(n, m + 1):
            if len(str(i)) == len(set(str(i))):
                cnt += 1
        print(cnt)
    except:
        exit()