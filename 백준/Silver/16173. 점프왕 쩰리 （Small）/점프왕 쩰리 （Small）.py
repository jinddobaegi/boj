# 정사각형 구역
# 출발점은 (0, 0)
# 구역 나가면 죽음
# 우, 하 방향만 감
# (N, N) 가면 끝
# 현재 칸에 쓰인 번호 == 한 번에 이동할 칸 수
# 게임에서 (N, N)에 도달할 수 있는지 확인

from collections import deque
q = deque()

N = int(input())
arr = list([] for i in range(N))
for i in range(N):
    arr[i] = list(map(int, input().split()))

# bfs? dfs?
# 재귀...?

# 이동 가능 거리에 따라
# for문으로 도착 가능 지점 구해서
# 거기 숫자로 또 다시 ㄱ

# 라고 생각했는데, 조건이 더 있는 것 같음
# 1) 이동 거리만큼 한 방향으로만 갈 수 있는 것 같음
# 2) 정확히 도착해야 도착이고, 넘어가면 안됨

res = 'Hing'

def my_search(r, c):
    global res

    # 범위 넘으면 컷
    if r < 0 or r >= N or c < 0 or c >= N:
        return

    # 도착하면 결과 저장 후 컷
    if arr[r][c] == -1:
        res = 'HaruHaru'
        return

    d = arr[r][c]  # 이동 가능 거리
    if d > 0:
            # 도착 지점 조합해서 다시 탐색
            my_search(r + d, c)
            my_search(r, c + d)
    else:
        return

my_search(0, 0)

print(res)