import sys
input = sys.stdin.readline

ls = {'NLCS': 'North London Collegiate School', 'BHA': 'Branksome Hall Asia', 'KIS': 'Korea International School', 'SJA': 'St. Johnsbury Academy'}
s = input().strip()
print(ls[s])