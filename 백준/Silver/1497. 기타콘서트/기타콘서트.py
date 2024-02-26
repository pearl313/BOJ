import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = [list(input().split()) for _ in range(n)]

def recur(cur, cnt, songs):
    global ans, max_val
    if cur == n:
        if cnt == 0:
            return
        
        play = set()
        for i in songs:
            for j in range(m):
                if ls[int(i)][1][j] == 'Y':
                    play.add(j)
                    
        if max_val <= len(play):
            max_val = len(play)
            ans = min(ans, len(songs))
        return
    
    recur(cur + 1, cnt + 1, songs + str(cur))
    recur(cur + 1, cnt, songs)
    
ans = 1e10
max_val = -1e10
recur(0, 0, '')
print(ans if max_val else -1)