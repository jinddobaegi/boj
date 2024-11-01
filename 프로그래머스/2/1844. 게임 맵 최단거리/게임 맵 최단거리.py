from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    def bfs(): 
        q = deque([(0, 0, 1)])  # 행, 열, cnt
        visited = [[0] * m for _ in range(n)]
        visited[0][0] = 1
        while q:
            i, j, cnt = q.popleft()
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] and not visited[ni][nj]:
                    if ni == n-1 and nj == m-1:
                        return cnt+1

                    q.append((ni, nj, cnt+1))
                    visited[ni][nj] = 1
        return -1
            
    
    return bfs()