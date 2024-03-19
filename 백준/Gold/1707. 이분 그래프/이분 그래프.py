from sys import stdin
from collections import deque

input = stdin.readline

# 정점의 집합을 둘로 분할
# 각 집합에 속한 정점끼리
# 서로 인접하지 않도록 분할할 수 있다 -> 이분 그래프

# 그러면, 한 정점에서
# 탐색 가능한 모든 정점, 즉 인접 정점이
# 나와 다른 집합에 속해야 함
# 그럼 현재 정점이 속한 집합도 알아야 하고
# 인접 노드의 방문 여부와 집합 일치 여부를 확인해야 함


K = int(input())


def bfs(node, group_num):
    # bfs를 돌면서
    # 인접 노드들을 이미 방문한 경우
    # 같은 집합에 속해있는지를 확인해야 함
    q.append(node)
    visited[node] = group_num
    while q:
        x = q.popleft()
        for y in adj_list[x]:  # 인접 노드에 대해
            if visited[y] == 0:  # 방문 안한 경우
                q.append(y)
                visited[y] = visited[x] * (-1)  # 방문 표시하며 집합까지 표시
            else:  # 방문한 경우? -> 집합 확인
                # 집합이 같다? NO
                if visited[x] == visited[y]:
                    return 'NO'
    return 'YES'


for tc in range(K):
    V, E = map(int, input().split())
    # 정점은 1~V까지 총 V개 있음
    # 간선은 E개임
    adj_list = list([] for _ in range((V+1)))
    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[v].append(u)
        adj_list[u].append(v)

    '''
    이걸로 집합이 같은지 다른지 표시하니까 시간초과 났었음
    list_a = []
    list_b = []
    
    visited에 1과 -1을 표시하는 방법으로 같은 집합인지 다른 집합인지 확인하더라
    '''

    # bfs
    q = deque()
    visited = [0]*(V+1)
    res = ''
    for i in range(1, V+1):
        if visited[i] == 0:
            res = bfs(i, 1)
            if res == 'NO':
                break

    print(res)
