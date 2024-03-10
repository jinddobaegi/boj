from sys import stdin
from collections import deque

input = stdin.readline

# M: 가로, N: 세로, H: 높이
M, N, H = map(int, input().split())

arr = list(list(list(map(int, input().split())) for _ in range(N)) for _ in range(H))
q = deque()
# 1: 익, 0: 안익, -1: 없
# 1) 일단 1인 곳 좌표 모두 que에 담고
# 2) bfs 수행
# 2-1) -1이 아닌 곳에 +1 해주고 해당 지점 좌표 append
# 2-2) bfs가 끝나고 한 군데서라도 0 나오면 res=-1


for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 1:
                q.append((h,n,m))  # z, y, x 좌표를 넣음

dz = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dx = [0,0,0,0,1,-1]


def bfs():
    while q:
        z, y, x = q.popleft()
        for k in range(6):
            nx, ny, nz = x+dx[k], y+dy[k], z+dz[k]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H:  # 범위 안에 있는지
                if arr[nz][ny][nx] == 0:  # 토마토가 있는지
                    arr[nz][ny][nx] = arr[z][y][x]+1  # 있으면 전+1 하고
                    q.append((nz,ny,nx))


bfs()

res = 0
isPossible = True  # 안 익은 거 있나 보는 용
for h in range(H):
    for n in range(N):
        for m in range(M):
            if arr[h][n][m] == 0:
                isPossible = False
            if res < arr[h][n][m]:
                res = arr[h][n][m]

if not isPossible:
    print(-1)
else:
    print(res-1)