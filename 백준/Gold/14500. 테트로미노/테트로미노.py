from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
visited = list([0] * M for _ in range(N))
max_v = 0

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

# 일직선 -> 2
# 정사각형 -> 1
# 니은자 -> 8
# 번개 -> 4
# 철 자 -> 4
# 총 19개?

# 500 * 500이라고 가정하면... 25000 * 19 -> 최대 약 50만번임
# 시간 초과 안 날 수도?
# 라고 생각하고 각 테트로미노마다 함수를 만드려 했으나
# 이건 아닌 것 같아서 찾아봄

# 철 자 제외 나머지는 dfs로 탐색이 가능
# 시작점과 세 번의 이동으로 도형 생성 가능


def dfs(r, c, cnt, val):
    global max_v

    if cnt == 4:
        max_v = max(max_v, val)
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, cnt+1, val+arr[nr][nc])
            visited[nr][nc] = 0


def t_shape(r, c):
    global max_v

    # 플러스 모양을 구하고
    # 하나를 빼는 식으로?
    val = arr[r][c]
    delta_values = []
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            val += arr[nr][nc]
            delta_values.append(arr[nr][nc])
    
    # 플러스 모양이 완성 안 되는 경우는 빼줄 필요가 없음
    if len(delta_values) == 4:
        for dv in delta_values:
            max_v = max(max_v, val-dv)
    else:
        max_v = max(max_v, val)


for y in range(N):
    for x in range(M):
        visited[y][x] = 1
        dfs(y, x, 1, arr[y][x])
        visited[y][x] = 0
        t_shape(y, x)

print(max_v)