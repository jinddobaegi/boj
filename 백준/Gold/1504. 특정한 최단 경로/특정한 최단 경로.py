from sys import stdin
import heapq

input = stdin.readline

#인접행렬로할까 인접리스트로 할까?
#인접행렬로 하면 메모리 초과가 날 것 같다.
#인접리스트로 하자.

INF = int(1e9)

# 시간초과...아무래도 

def dijkstra(start):
    distance_weight = [INF] * (N+1) # 1번 정점에서 N번 정점까지의 거리를 저장할 리스트
    distance_weight[start] = 0 # 시작점은 0으로 초기화

    q = [] # 우선순위 큐 생성
    heapq.heappush(q, (0, start)) # 시작점을 우선순위 큐에 저장

    while q:
        dist, now = heapq.heappop(q)
        if distance_weight[now] < dist: # 현재노드번호까지의 거리가 현재노드번호까지의 거리보다 작으면 넘어간다.
            continue
        for node, weight in graph[now]: # 현재조회된 노드번호와 연결된 노드번호와 거리를 조회
            cost = dist + weight
            if cost < distance_weight[node]: # 현재노드번호까지의 거리와 연결된 노드번호까지의 거리를 더한 값이 연결된 노드번호까지의 거리보다 작으면
                distance_weight[node] = cost
                heapq.heappush(q, (cost, node))
    return distance_weight

N, E = map(int, input().split()) # 정점의 개수 N, 간선의 개수 E

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split()) # a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그거리가 c    
    graph[a].append((b, c))
    graph[b].append((a, c))

# for i in graph:
#     print(i)


V, K = map(int, input().split()) # 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 V, K
# print("거처야하는 정점",V, K)

# 1번 정점에서 N번 정점까지의 거리를 저장할 리스트
distance_1 = dijkstra(1)
# V번 정점에서 N번 정점까지의 거리를 저장할 리스트
distance_V = dijkstra(V)
# K번 정점에서 N번 정점까지의 거리를 저장할 리스트
distance_K = dijkstra(K)

# print(distance_1)
# print(distance_V)
# print(distance_K)


# 1 -> V -> K -> N
# 1 -> K -> V -> N
# 두가지 경우를 비교해서 최소값을 출력

result = min(distance_1[V] + distance_V[K] + distance_K[N], distance_1[K] + distance_K[V] + distance_V[N])

if result >= INF:
    print(-1)
else:
    print(result)