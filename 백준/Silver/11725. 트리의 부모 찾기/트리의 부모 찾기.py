from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

adj_list = list(list() for _ in range(N+1))

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

parents = [0]*(N+1)
visited = [0]*(N+1)
q = deque()
q.append(1)
visited[1] = 1
tree = [0]*(N+1)


def bfs():
    while q:
        v = q.popleft()
        for w in adj_list[v]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)
                tree[w] = v


bfs()
for i in range(2,N+1):
    print(tree[i])