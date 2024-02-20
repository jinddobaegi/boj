import sys
sys.setrecursionlimit(10**6)

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def my_search(y, x):
    visited[y][x] = 1  # 현재 위치부터 방문처리하고

    for k in range(4):
        ny = y + dr[k]
        nx = x + dc[k]
        # 델타 탐색 범위가 전체 범위 내에 있고 방문 안했고 배추 있으면 ㄱ
        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and arr[ny][nx] == 1:
            my_search(ny, nx)
    else:
        return


for tc in range(T):
    M, N, K = map(int, input().split())

    arr = list([0] * M for i in range(N))  # 배추밭
    visited = list([0] * M for i in range(N))  # 방문 리스트
    cnt = 0  # 지렁이 수
    
    # 배추 심기
    for i in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1

    # 배추밭 탐색하다가 1 나오면
    # 방문 안했으면
    # 거기서 방문 가능한 곳 모두 탐색 및 방문 처리
    # 끝나면 cnt += 1 하고
    # 배추밭 탐색 재개

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                my_search(i, j)  # 탐색
                cnt += 1  # 끝나면 지렁이 뿌리기

    print(cnt)