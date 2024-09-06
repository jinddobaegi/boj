from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)

# N*N 땅
# 각 칸에는 인구 수 써있음
# 맞닿은 칸 인구 차이가 L 이상, R 이하라면 개방
# 연합을 이루고 있는 각 칸의 인구수는 평균이 됨(소수점 버림)
# "열고 => 이동 => 닫고" 반복하면
# 걸리는 일 수?

# 1) 전체를 돌아 연합들을 구하고
# 2) 각 연합의 인구로 업데이트
# 변화가 없을 때까지 반복

# 1.1) 상하좌우 인구차이 확인 => dfs로?
# 1.2) dfs가 종료되면 한 연합 완성

def dfs(i, j, f):
    f.append((i, j))
    visited[i][j] = 1
    for di, ji in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = i + di, j + ji
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and check_pop(i, j, ni, nj):
            dfs(ni, nj, f)

    return f


def check_pop(i1, j1, i2, j2):
    return L <= abs(arr[i1][j1] - arr[i2][j2]) <= R


def update_pop(fs):
    for f in fs:
        p = 0
        lf = len(f)
        for y, x in f:
            p += arr[y][x]

        p //= lf
        for y, x in f:
            arr[y][x] = p


N, L, R = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
cnt = 0
while True:
    feds = []
    visited = list([0] * N for _ in range(N))
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                fed = dfs(r, c, [])
                if len(fed) > 1:
                    feds.append(fed)

    if not feds:
        break

    update_pop(feds)
    cnt += 1

print(cnt)
