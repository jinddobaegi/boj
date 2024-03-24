from sys import stdin
import heapq  # 우선순위 큐

input = stdin.readline


# 1부터 N까지 도시
# M개의 단방향 도로
# 모든 도로의 거리는 1
# X로부터 최단거리가 K인 도시들의 번호를 출력

N, M, K, X = map(int, input().split())

adj_list = list([] for _ in range(N+1))
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)  # 단방향
    # 거리가 1이기 때문에, 거리 정보를 같이 저장하지 않음
    # 만약 거리의 가중치가 다르다면
    # (거리, 노드번호) 이런 식으로 adj_list를 만들자


# Dijkstra
# 방문한 지점이 있을 거고(visited 역할인데, 누적거리도 저장되는 visited임)
# 우선순위(pq) 큐를 사용
# pq에는 정점와 누적거리를 저장할 것임 (누적 거리 작은 순)
# 시작점과 누적거리 방문
# 1. 그 시점에서 갈 수 있는 곳과 누적거리들을 pq에 넣어줌
# 2. pq에 있는 거 하나 꺼내서 방문 쳌
# 1,2 반복
# 반복하다가 visited에 있는 정점이 겹친다면? 누적거리 비교해서 작은 거 남김
# 이렇게 도착점까지 반복

# 1. 누적 거리 저장
INF = int(1e9)
distance = [INF] * (N+1)  # 0번 안 씀


def dijkstra(s):
    # 2. 우선순위 큐
    pq = []

    # 출발점 초기화
    heapq.heappush(pq, (0, s))
    distance[s] = 0

    while pq:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, v = heapq.heappop(pq)

        # 이미 방문 + 누적 거리가 더 짧게 방문한 적 있으면 pass
        if distance[v] < dist:
            continue

        # 인접 노드를 확인
        for w in adj_list[v]:
            # w로 갔을 때 누적 거리 갱신
            new_cost = dist + 1  # 가중치가 다르다면 1 대신 이동할 노드에 대한 거리(cost) 써줘야겠지?

            # 누적 거리가 기존보다 크네?
            if distance[w] <= new_cost:
                continue

            distance[w] = new_cost
            heapq.heappush(pq, (new_cost, w))


dijkstra(X)

# X에서 이동할 수 있는 곳들의 최단거리가 distance에 저장돼있을 것임

if K not in distance:
    print(-1)
else:
    for i in range(1, N+1):
        if distance[i] == K:
            print(i)
