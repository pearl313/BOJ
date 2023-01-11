N = int(input())
pokemon = dict()
for _ in range(N):
    name = input()
    K, M = map(int, input().split())
    cnt = 0
    while K <= M:
        M -= K
        cnt += 1
        M += 2
    pokemon[name] = cnt
print(sum(pokemon.values()))
for key, value in pokemon.items():
    if value == max(pokemon.values()):
        print(key)
        break