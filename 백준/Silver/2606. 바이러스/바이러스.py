from collections import deque

# 노드 개수
# 간선 개수
# 간선 정보 주어짐

V = int(input())
E = int(input())

# bfs나 dfs 이용해서 모든 간선을 탐색해야 함

# bfs로 가자
# queue 이용
# 노드 담고
# 하나 빼면서 그거랑 연결된 거 담고
# queue 빌 때까지?

q = deque()
adj_list = list([] for _ in range(V+1))

for i in range(E):
    v1, v2 = map(int, input().split())
    # 연결 정보 추가
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

visited = [0] * (V+1)
# 시작은 무조건 1번 컴퓨터
q.append(1)
visited[1] = 1
res = 0

while q:
    # q에서 dq
    v = q.popleft()
    # v에 연결된 애들(w) 순환
    for w in adj_list[v]:
        # 방문 안 했으면
        if visited[w] != 1:
            q.append(w)  # q에 nq하고
            visited[w] = 1  # 방문 표시
            res += 1
    # q 맨 앞에 있는 애 빼서
    # v로 바꿈

print(res)
