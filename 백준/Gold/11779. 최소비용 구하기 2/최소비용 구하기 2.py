from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

N = int(input())
M = int(input())

graph = list([] for _ in range(N+1))
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

A, B = map(int, input().split())

# dijkstra는 pq와 distance가 존재
INF = int(1e9)
pq = []
distance = [INF] * (N+1)
dij_route = [0] * (N+1)

def dijkstra(start):
    # 시작점 초기화
    distance[start] = 0
    heappush(pq, (0, start))

    while pq:
        dist, v = heappop(pq)

        if distance[v] < dist:
            continue

        for cost, w in graph[v]:
            new_dist = dist + cost

            if distance[w] <= new_dist:
                continue

            distance[w] = new_dist
            dij_route[w] = v
            heappush(pq, (new_dist, w))


dijkstra(A)

print(distance[B])
# print(dij_route)

path = [B]
now = B
while now != A:
    now = dij_route[now]
    path.append(now)

# print(path)
path = path[::-1]
print(len(path))
print(*path, sep=' ')