import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna = [input().strip() for _ in range(n)]
ans = ''
distance = 0
for i in range(m):
    seq = {}
    for j in ('A', 'C', 'G', 'T'):
        seq[j] = [dna[k][i] for k in range(n)].count(j)
    ans += max(seq, key=seq.get)
    distance += n - max(seq.values())
print(ans, distance, sep='\n')