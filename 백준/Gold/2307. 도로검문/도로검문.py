from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def dijkstra(s):
    pq = []
    distance = [INF] * (N + 1)
    route = list([] for _ in range(N + 1))

    heappush(pq, (0, s))
    distance[s] = 0
    route[s].append(s)

    while pq:
        dist, v = heappop(pq)
        # pop하고 그 위치를 이전에 더 짧게 가본 적이 있는지 distance에서 확인
        if distance[v] < dist:
            continue
        # 그런 적 없으면 ㄱㄱ
        # 그 위치에서 이동 가능한 노드 확인
        for cost, w in adj_list[v]:
            # 간선 가중치 더해보고 그 이동할 위치를 더한 값보다 짧게 가본적 있는지 확인
            new_dist = dist + cost
            if distance[w] <= new_dist:
                continue

            heappush(pq, (new_dist, w))
            distance[w] = new_dist
            route[w] = route[v] + [w]

    return distance[N], route[N]


def blocked_dijkstra(s, x, y):
    pq = []
    distance = [INF] * (N + 1)
    route = list([] for _ in range(N + 1))

    heappush(pq, (0, s))
    distance[s] = 0
    route[s].append(s)

    while pq:
        dist, v = heappop(pq)
        if distance[v] < dist:
            continue

        for cost, w in adj_list[v]:
            # 이동시 막은 길이면 continue
            if v in (x, y) and w in (x, y):  # 양방향임을 고려
                continue

            new_dist = dist + cost
            if distance[w] <= new_dist:
                continue

            heappush(pq, (new_dist, w))
            distance[w] = new_dist
            route[w] = route[v] + [w]

    return distance[N], route[N]


# 도로는 모두 양방향
# 1: 진입, N: 퇴출
# 검문을 통해 얻는 최대 지연시간을 구하자
# 지연 효과 없으면 0
# 도시 탈출 못하게 하면 -1 출력

N, M = map(int, input().split())
adj_list = list([] for _ in range(N+1))  # 0 안 씀
for i in range(M):
    a, b, t = map(int, input().split())
    adj_list[a].append((t, b))
    adj_list[b].append((t, a))

# 다익스트라로 "경로"를 얻어서
# 그 경로에 있는 노드만 막아보면
# 지연시간 구할 수 있음

INF = int(1e9)
min_v, min_route = dijkstra(1)
r_len = len(min_route)

# route[N]에 탈출 경로 담겨있음
# 이 중 연결된 x-y 골라서 막았을 때
# 각각 다익스트라 해보자

blocked_min_v = 0
is_inf = False
for idx in range(1, r_len):
    b1 = min_route[idx-1]
    b2 = min_route[idx]
    # print(f'b1: {b1}, b2: {b2}')
    tmp_min_v, tmp_min_route = blocked_dijkstra(1, b1, b2)
    # print(tmp_min_v)
    # print(tmp_min_route)

    if tmp_min_v == INF:
        is_inf = True
        break

    blocked_min_v = max(tmp_min_v, blocked_min_v)

res = -1 if is_inf else blocked_min_v-min_v
print(res)