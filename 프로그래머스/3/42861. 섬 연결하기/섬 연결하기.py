from heapq import heappush, heappop

def solution(n, costs):
    answer = 0
    adj_list = [[] for _ in range(n)]
    for a, b, c in costs:
        heappush(adj_list[a], (c, b))
        heappush(adj_list[b], (c, a))
    
    pq = [(0, 0)]  # 비용, 노드
    visited = [0] * n
    cnt = 0
    while cnt < n:
        cv, v = heappop(pq)
        if visited[v]:
            continue
            
        visited[v] = 1
        answer += cv
        cnt += 1
        for cw, w in adj_list[v]:
            if not visited[w]:
                heappush(pq, (cw, w))
    
    return answer