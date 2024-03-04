# 연결 요소의 개수
# 실버 2
import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
board = [[] for _ in range(N+1)]
for i in range(M):
    # 간선의 양끝점 (해당 점들을 다 board에 담아줌)
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)


def dfs(board, v, visited):
    # 돌기 시작할 때 일단 방문 체크해줌
    visited[v] = True
    for i in board[v]:
        if not visited[i]:
            dfs(board, i, visited)


# 연결된 노드의 개수
cnt = 0

# 방문 지점 체크할 visited
visited = [False] * (N+1)
# 1부터 돌면서
for j in range(1, N+1):
    # 방문하지 않았다면 탐색 ㄱ
    if not visited[j]:
        dfs(board, j, visited)
        # 탐색 끝나면 체크하나씩 해주고
        cnt += 1

print(cnt)