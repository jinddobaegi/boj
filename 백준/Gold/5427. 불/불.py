from sys import stdin
from collections import deque

input = stdin.readline

# 불부터 bfs 후 상근이 bfs
# 상근이 bfs할 때 불이 붙은 시간을 보고 이동 가능 여부 판단


def bfs(is_man, q):
    global res

    while q:
        cnt, r, c = q.popleft()
        cnt += 1
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if arr[nr][nc] in '.@' and visited[nr][nc] > cnt:
                    q.append((cnt, nr, nc))
                    visited[nr][nc] = cnt
            elif is_man:
                res = cnt
                return

    return


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    arr = [[''] * w for _ in range(h)]
    visited = [[int(1e6)] * w for _ in range(h)]
    q_fire = deque()
    q_man = deque()
    si, sj = 0, 0
    for i in range(h):
        tmp = tuple(input().rstrip())
        for j in range(w):
            x = tmp[j]
            arr[i][j] = x
            if x == '*':
                si, sj = i, j
                q_fire.append((0, i, j))
                visited[i][j] = 0
            elif x == '@':
                q_man.append((0, i, j))
                # visited 표시는 불 이후에 하자

    res = "IMPOSSIBLE"
    bfs(0, q_fire)
    visited[si][sj] = 0
    bfs(1, q_man)
    print(res)