from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = 1
            q = deque([i])
            while q:
                v = q.popleft()
                for j in range(n):
                    if j == v:
                        continue
                    if computers[v][j] and not visited[j]:
                        q.append(j)
                        visited[j] = 1

    return answer