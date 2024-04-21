# 그래프 - 최소 비용 문제
# 1) 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리 -> MST
# 2) 두 정점 사이의 최소 비용의 경로 찾기 -> 다익스트라

# 신장트리
# 모든 정점을 연결
# 사이클 x, 부분 그래프 == 간선의 개수: n-1
# 한 그래프에서 여러개 나올 수 있음 -> 하나 찾고 끝내면 안된다!

# 최소 신장트리(MST)
# 신장트리 중, 간선들의 가중치의 합이 최소인 것

# 예시 문제,
# N개의 도시를 연결하는 도로를 건설하려 할 때,
# 모든 도시에 갈 수 있도록
# 가장 비용이 적게 들도록
# 도로를 건설

'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51

'''

from heapq import heappop, heappush
from sys import stdin

input = stdin.readline


V, E = map(int, input().split())
# 인접리스트 방식
graph = list([] for _ in range(V+1))  # for prim
edge = []                             # for kruskal

for _ in range(E):
    f, t, w = map(int, input().split())
    # for prim
    graph[f].append((w, t))
    graph[t].append((w, f))

    # for kruskal
    edge.append([f, t, w])

# 방법1) 한 정점에서 출발해서, 내가 갈 수 있는 곳들 중 제일 짧은 곳으로!
# 그리디의 일종
# 모든 정점을 방문할 때까지
# bfs랑 어느 정도 유사
# 우선순위 큐를 활용
# == Prim 알고리즘


def prim(start):
    pq = []
    # MST에 포함되었는지 여부
    visited = [0] * (V+1)

    # init
    heappush(pq, (0, start))  # weight, start
    # 누적합 저장
    total = 0

    while pq:
        # 가장 적은 가중치 가진 정점 꺼냄
        dist, now = heappop(pq)

        if visited[now]:  # 방문한 적 있으면 컷
            continue

        visited[now] = 1  # 방문한 적 없으면, 방문 체크
        total += dist  # 누적합 추가

        # 갈 수 있는 노드들을 체크
        for cost, next in graph[now]:
            # 이미 방문했다면 pass
            if visited[next]:
                continue

            # 아니라면
            heappush(pq, (cost, next))

    return total


# res1 = prim(1)
# print(res1)

# 방법2) 전체 간선들 중에 제일 가중치가 적은 곳부터 선택!
# 간선 정보를 정렬해야 함
# 전체 간선들 보고 제일 짧은 거리 순서로
# 기존 방문 여부
# 얘도 그리디 일종
# == Kruskal 알고리즘

# Prim이랑 차이점은 시작점을 안 정해도 된다는 것!
# 그냥 모든 간선 중 가장 짧은 것부터 시작!

# w를 기준으로 정렬
edge.sort(key=lambda x: x[2])

# 사이클 발생 여부를 union find로 해결
parents = [i for i in range(V+1)]


def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        # 사이클 발생
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def kruskal():
    cnt = 0  # 현재 방문한 정점 수
    total = 0  # 누적합
    for f, t, w in edge:
        # 사이클이 발생하지 않는다면
        if find_set(f) != find_set(t):
            cnt += 1
            total += w
            union(f, t)
            # MST 구성이 끝나면
            if cnt == V:
                break

    return total


res2 = kruskal()
print(res2)