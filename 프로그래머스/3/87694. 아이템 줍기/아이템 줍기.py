from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 'ㄷ'자에서 꼬이지 않도록 모든 좌표를 2배로 하자
    
    arr = [[-1]*102 for _ in range(102)]
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if y1 < i < y2 and x1 < j < x2:
                    arr[i][j] = 0
                elif arr[i][j] != 0:
                    arr[i][j] = 1
    
    # BFS
    q = deque([(characterY*2, characterX*2)])
    visited = [[-1] * 101 for _ in range(101)]
    visited[characterY*2][characterX*2] = 0
    while q:
        r, c = q.popleft()
        cnt = visited[r][c] + 1
        for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr, nc = r+dr, c+dc
            if 0 < nr < 101 and 0 < nc < 101 and arr[nr][nc] == 1 and visited[nr][nc] == -1:
                if nr == itemY*2 and nc == itemX*2:
                    return cnt//2
                q.append((nr, nc))
                visited[nr][nc] = cnt
    
    return answer