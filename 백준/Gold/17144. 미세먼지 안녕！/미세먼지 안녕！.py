from sys import stdin
from collections import deque

input = stdin.readline


def bfs():
    global arr

    while q:
        r, c, d = q.popleft()
        d //= 5
        cnt = 0
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if nr in (m1, m2) and nc == 0:
                    continue
                cnt += 1
                arr[nr][nc] += d
        arr[r][c] -= d*cnt

        
def purify(mr, dr, dc, is_clock_wise):
    r, c = mr, 0
    k = 0
    while True:
        nr, nc = r + dr[k], c + dc[k]
        if nr == mr and nc == 0:
            arr[r][c] = 0
            break
        elif not is_clock_wise and 0 <= nr <= mr and 0 <= nc < C:
            arr[r][c] = arr[nr][nc]
            r, c = nr, nc
        elif is_clock_wise and mr <= nr < R and 0 <= nc < C:
            arr[r][c] = arr[nr][nc]
            r, c = nr, nc
        else:
            k += 1
    arr[mr][0] = 0


R, C, T = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(R))
machines = []
q = deque()
for i in range(R):
    for j in range(C):
        x = arr[i][j]
        if x > 0:
            q.append((i, j, x))
        elif x == -1:
            machines.append(i)

m1 = machines[0]
m2 = machines[1]
for tc in range(T):
    bfs()
    purify(m1, (-1, 0, 1, 0), (0, 1, 0, -1), 0)
    purify(m2, (1, 0, -1, 0), (0, 1, 0, -1), 1)
    for i in range(R):
        for j in range(C):
            x = arr[i][j]
            if x > 0:
                q.append((i, j, x))

res = sum(map(lambda a: a[2], q))
print(res)