from sys import stdin
from collections import deque

input = stdin.readline

f, s, g, u, d = map(int, input().split())
# F: 전체 층수(범위)

# S: 강호 층(시작)
# G: 회사 층(목표)

# U: 위로 가는 층수
# D: 밑으로 가는 층수

res = 'use the stairs'

# 현재 위치를 최상위 노드로 가정
# 그 다음 이동 가능한 층을 노드로 놓고 차례로 방문하는 식
visited = [0] * (f+1)


def bfs():
    q = deque()
    q.append((s, 0))
    visited[s] = 1

    while q:
        floor, cnt = q.popleft()
        # 도착
        if floor == g:
            print(cnt)
            return

        for move in (u, -d):
            next_floor = floor + move
            # 범위 확인
            if 1 <= next_floor <= f:
                # 이동할 층 가봤으면 컷
                if visited[next_floor]:
                    continue

                visited[next_floor] = 1
                q.append((next_floor, cnt+1))

    print('use the stairs')


bfs()