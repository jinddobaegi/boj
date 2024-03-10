# 못 풀어서 결국 검색의 도움을 조금 받ㅇ...
# bfs를 이용
# 현재 위치를 최상위 노드에 넣고
# 그 다음 층에 이동 가능한 위치를 노드로 넣고 차례로 방문하는 식

from collections import deque

N, K = map(int, input().split())

check_points = [0] * 100001  # check_point[x]는 x의 이전 노드, 즉 부모 노드가 담김
time_lists = [0] * 100001     # distances[x]는 x까지 갈 때 걸리는 시간이 담김


def bfs():
    que = deque()
    que.append(N)
    while que:
        x = que.popleft()
        if x == K:
            print(time_lists[x])
            arr = []  # 여기에
            # 여태까지 경로 check_points 돌면서 배열 만들고 출력
            pr = x
            for _ in range(time_lists[x]+1):
                arr.append(pr)
                pr = check_points[pr]
            arr = arr[::-1]
            print(' '.join(map(str, arr)))
            return x

        for nx in (x+1, x-1, x*2):
            if 0<=nx<=100000 and time_lists[nx]==0:  # 범위 안에 있고 온 적 없으면
                que.append(nx)
                time_lists[nx] = time_lists[x]+1  # 이전 기록 + 1
                check_points[nx] = x


bfs()
