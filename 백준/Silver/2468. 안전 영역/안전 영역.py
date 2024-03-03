from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
arr = list(list(map(int, input().split())) for i in range(N))
max_v = 0

for i in range(N):
    for j in range(N):
        if max_v < arr[i][j]:
            max_v = arr[i][j]

max_cnt = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    que = deque()
    que.append((y, x))
    visited[y][x] = 1

    while que:
        y_pop, x_pop = que.popleft()
        for k in range(4):
            ny = y_pop + dy[k]
            nx = x_pop + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and arr[ny][nx]:
                    visited[ny][nx] = 1
                    que.append((ny, nx))


# 그냥 1부터 N까지 물 높이를 올려 가보자
# => N까지 할 게 아니라, 최댓값을 찾아서 걔까지 해야함
for n in range(1, max_v+1):
    # arr에서 n 이하인 지점 모두 0으로(잠기는 표시)
    for row in range(N):
        for col in range(N):
            if arr[row][col] <= n:
                arr[row][col] = 0

    cnt = 0  # 이번 물 높이에서의 안 잠긴 지역 개수 cnt 하기 위함
    visited = list([0] * N for _ in range(N))  # visited 초기화
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and arr[r][c]:
                cnt += 1
                bfs(r, c)

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)