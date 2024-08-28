from sys import stdin
from collections import deque

input = stdin.readline

# 1) 임티 모두복사
# 2) 클립보드 내용 붙여넣기
# 3) 화면 임티 중 하나 삭제

# 모든 연산은 1초가 걸린다
# 화면에 이모티콘 1개가 존재하는 상태에서
# S개의 이모티콘 만드는 데 걸리는 최소 시간

S = int(input())
INF = int(1e9)

# bfs 써가면서
# 특정 개수의 최솟값을 업데이트 해가면서
# S에 도달해보자

def bfs():
    q = deque()  # 임티개수, 클립보드 개수
    q.append((1, 0))
    counter = list([INF] * (S+2) for _ in range(S+2))  # 행: 이모지 수, 열: 클립보드 수, 값: cnt
    counter[1][0] = 0
    while q:
        emoji, cb = q.popleft()
        # 복사
        if 0 < emoji <= S+1 and counter[emoji][emoji] == INF:
            q.append((emoji, emoji))
            counter[emoji][emoji] = counter[emoji][cb] + 1

        # 붙여넣기
        if cb:
            x = emoji + cb  # emoji 개수에 클립보드의 c를 붙여넣기한 개수 == x
            if 0 < x <= S+1 and counter[x][cb] == INF:
                q.append((x, cb))
                counter[x][cb] = counter[emoji][cb] + 1

        # 한 개 삭제
        if 0 < emoji-1 and counter[emoji-1][cb] == INF:
            q.append((emoji-1, cb))
            counter[emoji-1][cb] = counter[emoji][cb] + 1

    return min(counter[S])


print(bfs())