from sys import stdin
from itertools import permutations

input = stdin.readline

N, M = map(int, input().split())
arr = [x for x in range(1, N+1)]
ps = permutations(arr, M)
for p in ps:
    print(*p)