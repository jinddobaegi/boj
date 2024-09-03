from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
arr = list(input().rstrip() for _ in range(N))

coins = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'o':
            coins.append((i, j))

c1, c2 = coins[0], coins[1]
visited_set = set()
visited_set.add((c1, c2))
q = deque([(c1, c2, 0)])
res = -1
while q and res == -1:
    coin1, coin2, cnt = q.popleft()
    if cnt >= 10:
        continue
    cnt += 1
    i1, j1 = coin1
    i2, j2 = coin2
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni1, nj1 = i1+di, j1+dj
        ni2, nj2 = i2+di, j2+dj

        p1 = 0 <= ni1 < N and 0 <= nj1 < M  # 동전1 안 빠졌나?
        p2 = 0 <= ni2 < N and 0 <= nj2 < M  # 동전2 안 빠졌나?

        # 둘 다 범위 안
        if p1 and p2:
            # 벽 있는 경우 고려한 위치 조정
            if arr[ni1][nj1] == '#':
                ni1, nj1 = i1, j1
            if arr[ni2][nj2] == '#':
                ni2, nj2 = i2, j2

            # 겹치는 경우 => 컷
            if ni1 == ni2 and nj1 == nj2:
                continue

            # 둘다 살아있고 안 겹치는 경우
            c1 = (ni1, nj1)
            c2 = (ni2, nj2)
            if (c1, c2) not in visited_set:  # 방문 안 한 경우
                q.append((c1, c2, cnt))
                visited_set.add((c1, c2))

        # 하나만 빠진 경우
        elif (p1 and not p2) or (p2 and not p1):
            res = cnt
            break

print(res)