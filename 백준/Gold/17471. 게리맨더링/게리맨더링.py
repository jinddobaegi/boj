from sys import stdin
from itertools import combinations

input = stdin.readline


def dfs(v, other_group):
    visited[v-1] = 1
    for w in adj_list[v-1]:
        if not visited[w-1] and w not in other_group:
            dfs(w, other_group)


N = int(input())  # 도시의 수
populations = list(map(int, input().split()))  # 1~N번 구역의 인구

adj_list = list([] for _ in range(N))  # 1~N번 구역 인접 리스트
for n in range(N):
    x, *adj_cities = map(int, input().split())
    adj_list[n] = adj_cities

# 도시를 두 부분으로 나눠서
# adj_list와 bfs/dfs를 통해 끊긴 부분이 있는지 check (visited가 다 찍히는지 보자)
# 끊긴 부분이 없다면, 두 부분의 인구 총합의 차를 구해서 최소가 되도록 한다

min_v = 10000

# 1) 두 부분집합으로 나누기
cities = set(x for x in range(1, N+1))
for i in range(1, (N//2)+1):
    A_list = set(combinations(cities, i))  # i개를 뽑은 부분집합의 모임, i: 1 ~ N-1
    for A in A_list:
        B = list(set(cities) - set(A))
        A = list(A)

        # 2) 각 부분집합 dfs 돌기
        visited = [0] * N
        # 2-1) A에 대해 dfs
        dfs(A[0], B)
        # 2-2) B에 대해 dfs
        dfs(B[0], A)

        # 하나라도 방문 안한 게 있으면 continue
        # is_A_ok = True
        # is_B_ok = True
        isOk = True
        for j in range(N):
            if not visited[j]:
                isOk = False
                break

        if not isOk:
            continue

        # 3) 두 부분 인구 총합 구하기, 차 구해서 최솟값으로 갱신
        # 3-1) A, for문 돌면서 인구 총합
        cnt_A = 0
        for a in A:
            cnt_A += populations[a-1]
        # 3-2) B, for문 돌면서 인구 총합
        cnt_B = 0
        for b in B:
            cnt_B += populations[b-1]

        tmp_v = abs(cnt_A - cnt_B)
        if min_v > tmp_v:
            min_v = tmp_v

res = -1 if min_v == 10000 else min_v
print(res)
