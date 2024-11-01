def solution(tickets):
    answer = []
    
    graph = dict()
    for a, b in tickets:
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
    
    for k, v in graph.items():
        v.sort(reverse=True)
    
    s = ['ICN']
    while s:
        v = s[-1]
        if v in graph and len(graph[v]) > 0:
            w = graph[v].pop()
            s.append(w)
        else:
            answer.append(s.pop())
        
    return answer[::-1]