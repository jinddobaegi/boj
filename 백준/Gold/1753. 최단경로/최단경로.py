from sys import stdin
import heapq

input = stdin.readline

# V: 정점 수, E: 간선 수
V, E = map(int, input().split())

K = int(input())  # 시작 정점 번호

adj_list = list([] for _ in range(V+1))
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((w, v))  # (가중치, 다음 노드)

# 다익스트라는
# pq와 distance가 존재
# pq에는 연결된 노드와 거기로 갔을 때의 누적 거리가 담김
# distance에는 시작점에서 각 정점까지의 최단 거리가 나옴

INF = int(1e9)

pq = []
distance = [INF] * V


def dijkstra(x):
    # 시작점 초기화
    heapq.heappush(pq, (0, x))  # 누적된 거리와 정점 삽입
    distance[x-1] = 0  # 시작점 to 시작점 -> 0 저장

    while pq:
        dist, v = heapq.heappop(pq)
        # 1) 현재 노드와 2) 이동할 노드에 대한 "거리 비교" 필요

        # 1) 현재 노드 더 짧게 가본 적 있는지?
        if distance[v-1] < dist:  # 얘는 이동하기 전에 확인하는 거라 등호가 안들어감
            continue

        for cost, w in adj_list[v]:
            new_cost = dist + cost

            # 2) 이동할 노드 더 짧게 가본 적 있는지?
            if distance[w-1] <= new_cost:  # 얘는 이동해보고 판단하는 거라 등호가 들어감
                continue

            # 여기까지 오면 이동해야됨
            distance[w-1] = new_cost
            heapq.heappush(pq, (new_cost, w))


dijkstra(K)

for d in distance:
    if d == INF:
        print('INF')
    else:
        print(d)

