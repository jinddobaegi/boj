from collections import deque

N, M = map(int, input().split())
computers = list(list() for _ in range(N+1))

# i번째 배열
# i번째 컴퓨터"를" 신뢰하는 컴퓨터들의 번호

for _ in range(M):
    a, b = map(int, input().split())
    computers[b].append(a)


def bfs(i):
    q = deque()
    visited = [0] * (N+1)
    q.append(i)
    visited[i] = 1

    cnt = 0
    while q:
        trusted = q.popleft()
        for trusting in computers[trusted]:
            if not visited[trusting]:
                q.append(trusting)
                visited[trusting] = 1
                cnt += 1

    return cnt

res = []
max_v = 0
for i in range(1, N+1):
    cnt = bfs(i)
    if max_v < cnt:
        max_v = cnt
        res = [i]
    elif max_v == cnt:
        res.append(i)

print(*res)