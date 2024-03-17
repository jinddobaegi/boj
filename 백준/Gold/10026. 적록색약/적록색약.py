# R / G / B 각 구역
# RG / B 구역

# bfs를 깔별로 돌려야하나?

from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

arr = list(list(input().rstrip() for _ in range(N)))
visited = list([''] * N for _ in range(N))

dr = (0,0,1,-1)
dc = (1,-1,0,0)


# bfs를 색깔 별로 돌아야 할 듯?
def bfs(i, j, color):
    q = deque()
    # 시작점 설정
    q.append((i, j))
    visited[i][j] = arr[i][j]

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0<=nr<N and 0<=nc<N:
                if not visited[nr][nc] and arr[nr][nc] == arr[r][c]:
                    q.append((nr, nc))
                    visited[nr][nc] = color


def bfs2(i, j, color):
    if color in ('R', 'G'):
        color = 1
    else:
        color = 2

    q = deque()
    # 시작점 설정
    q.append((i, j))
    visited[i][j] = color

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0<=nr<N and 0<=nc<N:
                if arr[nr][nc] in ('R', 'G'):
                    new_color = 1
                else:
                    new_color = 2
                if not visited[nr][nc] and new_color == color:
                    q.append((nr, nc))
                    visited[nr][nc] = color


cnt = 0

for m in range(N):
    for n in range(N):
        if not visited[m][n]:
            cnt += 1
            bfs(m, n, arr[m][n])


visited = list([''] * N for _ in range(N))
cnt2 = 0

for m in range(N):
    for n in range(N):
        if not visited[m][n]:
            cnt2 += 1
            bfs2(m, n, arr[m][n])

print(cnt, cnt2)
