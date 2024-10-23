from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

# A에서 B 가는 최소비용

n = int(input())
m = int(input())
adj_list = list(list() for _ in range(n+1))
for _ in range(m):
    a, b, w = map(int, input().split())
    adj_list[a].append((w, b))

s, e = map(int, input().split())

def dijkstra(n, adj_list, s, e):
    INF = int(1e8)
    pq = []
    distance = [INF] * (n+1)
    pq.append((0, s))
    distance[s] = 0
    while pq:
        dist, v = heappop(pq)
        if distance[v] < dist:
            continue
        for cost, w in adj_list[v]:
            new_dist = dist + cost
            if distance[w] <= new_dist:
                continue
            distance[w] = new_dist
            heappush(pq, (new_dist, w))

    return distance[e]

print(dijkstra(n, adj_list, s, e))