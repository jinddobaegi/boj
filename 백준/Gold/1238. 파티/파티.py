from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

# N: 노드 수, M: 간선 수, X: 도착지
N, M, X = map(int, input().split())

# X에 모여서 파티함
# "i -> X"가 가장 긴 사람

graph = list([] for _ in range(M+1))
for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((d, e))

INF = int(1e9)

def dijkstra(start, end):
    distance = [INF] * (N + 1)
    pq = []

    distance[start] = 0
    pq.append((0, start))

    while pq:
        dist, v = heappop(pq)

        if distance[v] < dist:
            continue

        for cost, w in graph[v]:
            new_dist = dist + cost

            if distance[w] <= new_dist:
                continue

            distance[w] = new_dist
            heappush(pq, (new_dist, w))

    return distance[end]


max_v = 0
for i in range(1, N+1):
    time1 = dijkstra(i, X)
    time2 = dijkstra(X, i)
    tmp = time1 + time2
    if max_v < tmp:
        max_v = tmp

print(max_v)

