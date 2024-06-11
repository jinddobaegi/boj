from sys import stdin
from heapq import heappush as hppush, heappop as hppop

input = stdin.readline

# 1 -> N 최단거리 이동
# BUT 임의로 주어진 두 정점을 통과해야 함

N, E = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(E):
    a, b, w = map(int, input().split())
    adj_list[a].append((w, b))
    adj_list[b].append((w, a))

waypoint_1, waypoint_2 = map(int, input().split())  # 경유지


def dijkstra(s, e):
    pq = []
    distance = [INF] * (N + 1)

    hppush(pq, (0, s))
    distance[s] = 0

    while pq:
        dist, v = hppop(pq)
        if distance[v] < dist:
            continue

        for cost, w in adj_list[v]:
            new_dist = dist + cost
            if distance[w] <= new_dist:
                continue
            hppush(pq, (new_dist, w))
            distance[w] = new_dist

    return distance[e]


a = dijkstra(1, waypoint_1)
b = dijkstra(waypoint_2, N)
c = dijkstra(waypoint_1, waypoint_2)
d = dijkstra(waypoint_1, N)
e = dijkstra(1, waypoint_2)

res = min(a+b, d+e)+c

print(res if res < INF else -1)