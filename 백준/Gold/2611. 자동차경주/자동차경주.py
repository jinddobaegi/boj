from sys import stdin, setrecursionlimit
from heapq import heappush, heappop

input = stdin.readline
setrecursionlimit(10**6)

N = int(input())
M = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    p, q, r = map(int, input().split())
    adj_list[p].append((q, r))

# dp적 사고를 해보자
# 사이클이 안 생김(예제만 그런 건가..?)
# 특정 노드까지 도달하는 최댓값을 저장


def my_func(s):
    dp = [[0, []] for _ in range(N+1)]
    dp[s][1] = [s]
    pq = []
    heappush(pq, (0, s))  # 거리, 노드 순

    while pq:
        dist, v = heappop(pq)
        # 이전에 더 큰 점수를 얻은 적 있는지?
        if dp[v][0] > dist:
            continue

        route_before = dp[v][1]  # 이전 경로
        for w, cost in adj_list[v]:
            new_dist = dist + cost

            if dp[w][0] >= new_dist:
                continue

            dp[w][0] = new_dist
            dp[w][1] = route_before + [w]  # 현재 경로

            if w != 1:  # 1이면 또 돌 필요 없음
                heappush(pq, (new_dist, w))

    return dp[1]


res = my_func(1)
print(res[0])
print(*res[1])