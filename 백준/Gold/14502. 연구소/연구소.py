from sys import stdin
from itertools import combinations
from collections import deque
from copy import deepcopy

input = stdin.readline

# 바이러스는 상하좌우로 퍼짐
# 세 칸에 벽을 세워서 만들 수 있는
# 안전영역의 최대 크기

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

# 그냥 모든 경우의 벽을 세워보자
com_list = []
for i in range(N):
    for j in range(M):
        com_list.append((i, j))

combs = list(combinations(com_list, 3))
q = deque()


def bfs(r, c):
    q.append((r, c))
    visited[r][c] = 1

    while q:
        r, c = q.popleft()

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if (lab_copy[nr][nc] == 0 or lab_copy[nr][nc] == 2) and visited[nr][nc] == 0:
                    lab_copy[nr][nc] = 2
                    visited[nr][nc] = 1
                    q.append((nr, nc))


max_v = 0
for comb in combs:
    visited = list([0] * M for _ in range(N))
    lab_copy = deepcopy(lab)
    # comb 하나에 좌표 세 개 들어있음
    # 그럼 그거에 벽 세웠을 때의 안전 구역을 각각 구해보자

    flag = True
    for y, x in comb:
        if lab_copy[y][x] == 0:
            lab_copy[y][x] = 1
        else:
            flag = False
            break

    if not flag:
        continue

    # 돌리고
    for n in range(N):
        for m in range(M):
            if lab_copy[n][m] == 2:
                bfs(n, m)
    tmp = 0
    # 안전구역 체크
    for r in range(N):
        for c in range(M):
            if lab_copy[r][c] == 0:
                tmp += 1

    max_v = max(max_v, tmp)


print(max_v)