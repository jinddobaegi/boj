from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
adj_list = list(set() for _ in range(N+1))
adj_list[0].add(1)
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].add(b)
    adj_list[b].add(a)

route = tuple(map(int, input().split()))

# 어차피 bfs는
# 같은 깊이에 있는 것들을 다 돌고 난 뒤
# 그 다음 깊이의 노드를 돌 수 있다

def bfs():
    q = deque()
    q.append(0)
    idx = 0  # 디큐 느낌으로 쓰는 것
    for w in route:  # 주어진 노드 순서대로 확인해볼 것임
        # 프론트 노드의 자식 중 w를 찾을 때까지 돎
        while w not in adj_list[q[idx]]:
            idx += 1  # 프론트 노드 자식 중에 w 없으면 디큐
            if idx == len(q):  # 큐가 빈 상태
                return 0
        q.append(w)  # 프론트의 자식 중 w가 있어서 while문 빠져나오고 인큐
        
    return 1  # for 문을 다 돌았다? == 마지막 경로까지 append 됐다


print(bfs())