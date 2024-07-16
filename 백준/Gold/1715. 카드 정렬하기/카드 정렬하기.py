from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

# 카드를 두 묶음 씩 합치는데
# 현재 묶인 것 포함해서
# 그 중 가장 작은 것 두 개씩 골라서 묶으면 됨

N = int(input())
pq = []

for _ in range(N):
    heappush(pq, int(input()))

len_of_decks = N
res = 0
while len_of_decks > 1:
    a = heappop(pq)
    b = heappop(pq)
    tmp = a+b
    res += tmp
    heappush(pq, tmp)
    len_of_decks -= 1

print(res)