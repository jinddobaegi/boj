from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    counter = [-1] * (n+1)
    q = deque([1])
    counter[1] = 0
    while q:
        v = q.popleft()
        cnt_w = counter[v]+1
        for w in graph[v]:
            if counter[w] == -1:
                q.append(w)
                counter[w] = cnt_w
    max_v = max(counter)
    for c in counter:
        if c == max_v:
            answer += 1
    
    return answer