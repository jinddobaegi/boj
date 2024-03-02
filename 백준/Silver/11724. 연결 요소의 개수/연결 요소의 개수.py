from sys import stdin
from collections import deque

input = stdin.readline

# N: 정점 개수, M: 간선 수
N, M = map(int, input().split())
adj_list = list(list() for i in range(N+1))  # 0은 안 쓸 거임

for i in range(M):
    u, v = map(int, input().split())
    # 무향그래프
    adj_list[u].append(v)
    adj_list[v].append(u)

# 1번 정점부터 돌기
# 한 번 돌면, 그 다음 정점 돌 차례
# 이미 탐색한 연결 요소들에 포함되어있는지 확인(visited)
# 안 돼있을 때만 탐색
# 총 묶음을 cnt로 세면 될 듯?

visited = [0] * (N+1)
que = deque()


def bfs():
    cnt = 0
    for node in range(1, N+1):
        # 해당 노드 방문기록 확인
        if visited[node] == 0:
            que.append(node)  # 담고 시작
            visited[node] = 1
            cnt += 1
            while que:
                n1 = que.popleft()
                for n2 in adj_list[n1]:
                    if visited[n2] == 0:
                        que.append(n2)
                        visited[n2] = 1

    return cnt


print(bfs())