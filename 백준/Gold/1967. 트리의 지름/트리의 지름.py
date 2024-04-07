from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)

'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10

'''

N = int(input())

graph = list([] for _ in range(N+1))
visited = [-1] * (N+1)

for _ in range(N-1):
    p, c, w = map(int, input().split())
    graph[p].append((w, c))
    graph[c].append((w, p))

def dfs(v, dist):
    visited[v] = dist
    for cost, w in graph[v]:
        if visited[w] == -1:
            dfs(w, dist + cost)

dfs(1, 0)

longest = max(visited)
start_node = visited.index(longest)

visited = [-1] * (N+1)
dfs(start_node, 0)

print(max(visited))
