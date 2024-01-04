mushrooms = list(int(input()) for _ in range(10))
total = 0
gap_ls = []
for i in range(10):
    total += mushrooms[i]
    gap_ls.append(abs(100 - total))
idx = gap_ls.index(min(gap_ls))
if gap_ls.count(min(gap_ls)) == 2:
    idx += 1
print(sum(mushrooms[:idx + 1]))
