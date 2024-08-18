from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

N = int(input())  # 도시 개수
M = int(input())  # 버스 개수
lines = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    lines[a].append((c, b))

# 목표
# 1) i번째 줄에 i-j 최소비용들 출력 => 총 N개(==도시 수)
# 2) i-j 최소비용일 때의 개수, 경로를 출력(출/도 포함)
# 1, 2 모두 경로가 없다면 0만 출력

def dijkstra(s):
    pq = []
    distances = [INF] * N
    routes = [[] for _ in range(N)]
    heappush(pq, (0, s))
    distances[s-1] = 0
    routes[s-1] = [s]

    while pq:
        dist, v = heappop(pq)
        route = routes[v-1]
        if distances[v-1] < dist:
            continue

        for cost, w in lines[v]:
            new_dist = dist + cost
            if distances[w-1] <= new_dist:
                continue
            distances[w-1] = new_dist
            heappush(pq, (new_dist, w))
            routes[w-1] = route + [w]

    for idx, d in enumerate(distances):
        if d == INF:
            distances[idx] = 0
    return distances, routes


INF = int(1e9)
distances = []
routes = []

for i in range(1, N+1):
    ds, rs = dijkstra(i)
    distances.append(ds)
    routes.append(rs)

for i in range(N):
    print(*distances[i])

for i in range(N):
    for route in routes[i]:
        if len(route) == 1:
            print(0)
        else:
            print(len(route), end=' ')
            print(*route)