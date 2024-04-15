from sys import stdin
from heapq import heappop, heappush

input = stdin.readline


N, D = map(int, input().split())

graph = list([] for _ in range(D+1))

# 이 부분은 검색했슴다..
for i in range(D):
    graph[i].append((1, i+1))

for _ in range(N):
    s, e, d = map(int, input().split())
    if e > D:
        continue
    graph[s].append((d, e))

# dijkstra 하려면 pq와 distance가 필요
INF = int(1e9)
pq = []
distance = [INF] * (D+1)


def dijkstra(start):
    # 시작점 초기화
    heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, v = heappop(pq)

        if distance[v] < dist:
            continue

        for cost, w in graph[v]:
            new_cost = dist + cost

            if distance[w] <= new_cost:
                continue

            distance[w] = new_cost
            heappush(pq, (new_cost, w))


dijkstra(0)

print(distance[D])
