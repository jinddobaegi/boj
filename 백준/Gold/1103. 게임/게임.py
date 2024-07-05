from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

# H: 구멍
# (0, 0)에서 시작
# 해당 숫자만큼 상하좌우로 움직일 수 있음
# 구멍에 빠지지 않는 최대 이동 횟수 구하기
# 무한 이동 가능하면 -1 출력
# 갔던 곳을 다시 가면 무한 이동 가능한 것!

N, M = map(int, input().split())
arr = list(input().rstrip() for _ in range(N))
visited = list([0] * M for _ in range(N))
dp = list([-1] * M for _ in range(N))
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
max_v = 0


def dfs(r, c, cnt):
    global max_v

    if max_v == -1:
        return

    if dp[r][c] >= cnt:
        return

    visited[r][c] = 1
    dp[r][c] = cnt
    max_v = max(cnt, max_v)
    x = int(arr[r][c])

    for k in range(4):
        nr = r + dr[k] * x
        nc = c + dc[k] * x

        # 이동 가능한지?
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 'H':
            # 방문한 적 있다? == 무한 이동 가능
            if visited[nr][nc]:
                max_v = -1
                return

            # 방문한 적 없으면 dfs
            else:
                dfs(nr, nc, cnt+1)
                visited[nr][nc] = 0  # 이 부분을 이용하여 매 시도마다 방문 기록을 초기화해야 함

        # 동전을 놓을 순 없어도 마지막 이동 횟수는 셈
        else:
            if max_v != -1:
                max_v = max(cnt+1, max_v)


dfs(0, 0, 0)
print(max_v)
