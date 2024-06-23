from sys import stdin
from collections import deque

input = stdin.readline

# 상어 최초 크기: 2
# 크기가 같은 물고기 -> 패스
# 크기가 작은 물고기 -> 먹음
# 크기가 큰 물고기 -> 블락

# 자기보다 작은 물고기 없으면 끝
# 거리 같으면 상, 좌 순

# 크기가 x일 때, x마리 먹어야 크기 1 증가
# 물고기 최대한 많이 먹을 때까지 몇 초?

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))

# 1~6: 물고기 크기
# 9: 상어

# 상어 위치랑 물고기 개수 파악
shark_loc = (0, 0)
fishes = [0] * 7  # 1~6 사이즈 물고기 개수
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark_loc = (i, j)
            arr[i][j] = 0
        elif arr[i][j]:
            fishes[arr[i][j]] += 1
# 상어의 위치에서 bfs 돌리면서 tmp로 몇번 갔는지 임시 카운트
# 0이거나 같으면 이동 가능
# 자기보다 크면 못감
# 자기보다 작은 걸 찾을 때까지 탐색
# 가장 가까운 것 중 가장 좌/상단에 있는 물고기 먹고
# 상어위치, cnt, 물고기 개수 업데이트
# 먹을 때마다 자기보다 큰 것만 남아있는지 확인해서 미리 종료시켜볼까

def bfs(r, c):
    q = deque([(1, r, c)])  # 횟수, 좌표
    visited = list([0] * N for _ in range(N))
    visited[r][c] = 1  # 횟수로 저장할 것임
    tmp_fishes = []

    while q:
        tmp, y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                point = arr[ny][nx]
                if point == 0 or point == shark_size:  # 지나가~
                    q.append((tmp+1, ny, nx))
                    visited[ny][nx] = tmp+1
                elif 0 < point < shark_size:  # 먹을 수 있는 거~
                    tmp_fishes.append((tmp, ny, nx))
                    visited[ny][nx] = tmp+1

    return tmp_fishes


cnt = 0  # 시간
eat = 0  # 먹은 수
dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
shark_size = 2
total = sum(fishes)
is_able = True
while total and is_able:
    candidates = bfs(*shark_loc)  # 가까운 물고기를 찾음

    if candidates:
        candidates.sort(key=lambda x: (x[0], x[1], x[2]))  # 이동 횟수, 행, 열 순 정렬
        tmp_cnt, r, c = candidates[0]
        # print(f"이동카운트: {tmp_cnt}, 좌표: ({r, c})")
        shark_loc = (r, c)  # 위치 갱신
        cnt += tmp_cnt  # 시간 갱신
        arr[r][c] = 0  # 뇸
        fishes[arr[r][c]] -= 1  # 물고기 마리 수 갱신
        total -= 1
        eat += 1  # 먹은 거
        if shark_size == eat:
            shark_size += 1
            eat = 0
    else:
        is_able = False

print(cnt)