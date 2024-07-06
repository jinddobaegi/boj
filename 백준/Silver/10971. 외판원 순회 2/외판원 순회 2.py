from sys import stdin

input = stdin.readline

# N개의 도시
# 출발지에서 모든 도시를 거쳐서 돌아와야 함
# 출발지를 제외한 나머지 도시는 한 번만 거쳐갈 수 있음
# 최소 비용


def dfs(f, cnt, dist):
    global min_v

    if cnt == N and f == start:
        min_v = min(dist, min_v)
        return

    for t, cost in adj_list[f]:
        if not visited[t]:
            visited[t] = 1
            dfs(t, cnt+1, dist + cost)
            visited[t] = 0


N = int(input())
adj_list = list([] for _ in range(N))
for i in range(N):
    tmp = tuple(map(int, input().split()))
    for j, x in enumerate(tmp):
        if x:
            adj_list[i].append((j, x))

# dfs로 가면서
# 거리 합하고
# 출발지 나오면 거리 갱신

min_v = int(1e8)  # 최대가 1e7
visited = [0] * N
start = 0
dfs(start, 0, 0)
print(min_v)