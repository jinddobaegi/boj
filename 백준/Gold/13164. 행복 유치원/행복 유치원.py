from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

# N명 키순으로 세움
# K묶음 만듦(한 조에 한 명 가능)
# 총비용 최소화

N, K = map(int, input().split())  # N은 30만까지
arr = tuple(map(int, input().split()))  # 오름차순 정렬 -> 키는 같을 수 있음
min_v = int(1e9)
pq = []

for i in range(N-1):
    heappush(pq, -(arr[i+1] - arr[i]))

for _ in range(K-1):
    heappop(pq)

print(-sum(pq))