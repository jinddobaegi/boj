from sys import stdin
from collections import deque

input = stdin.readline

# 공기청정기 크기: 2 * 1
# 1초동안 다음 일이 일어남
# 미세먼지는 동서남북으로 확산(미세먼지가 있는 모든 칸에서 일어남)
# 확산될 때의 양은 1//5 만큼
# 원래 있던 곳은 확산된 만큼 줄어듦
# 공기청정기에서 바람이 나온다
# 위에는 반시계, 아래는 시계방향으로 순환한다
# 바람 불면 바람 방향대로 한 칸씩 이동
# 공기청정기로 들어가면 없어짐

# 접근 방법
# 동시에 확산되는 걸 어떻게 해야될까?!
# bfs를 사용한다고 가정
# 큐에 미세먼지의 위치만 있다면 => 매번 변경된 미세먼지 양이 제대로 업데이트가 안 될 것임
# 따라서 매 초마다
# 전체 배열에서 미세먼지 위치를 q에 담고 bfs => 변화량을 arr에 업데이트
# 공기청정기 순환 및 정화

def bfs():
    global arr

    while q:
        r, c, d = q.popleft()
        d //= 5
        cnt = 0
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if nr in (m1, m2) and nc == 0:  # 공기청정기쪽이면 컷
                    continue
                cnt += 1
                arr[nr][nc] += d
        arr[r][c] -= d*cnt


def purify(mr, dr, dc, is_clock_wise):
    # 반시계 방향의 경우 오히려 (m1, 0)부터 시계방향으로 당겨보자
    r, c = mr, 0
    k = 0
    while True:
        nr, nc = r + dr[k], c + dc[k]
        if nr == mr and nc == 0:
            arr[r][c] = 0
            break

        # 반시계방향
        elif not is_clock_wise and 0 <= nr <= mr and 0 <= nc < C:
            arr[r][c] = arr[nr][nc]
            r, c = nr, nc

        # 시계방향
        elif is_clock_wise and mr <= nr < R and 0 <= nc < C:
            arr[r][c] = arr[nr][nc]
            r, c = nr, nc

        else:
            k += 1
            # k = (k+1)%4
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