from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

N = int(input())  # 대학의 수
lectures = list(tuple(map(int, input().split())) for _ in range(N))  # p, d 순
lectures.sort(key=lambda x: x[1])  # 마감기한 짧은 순 정렬


pq = []
for p, d in lectures:
    heappush(pq, p)
    if d < len(pq):
        heappop(pq)

print(sum(pq))