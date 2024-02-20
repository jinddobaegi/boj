from collections import deque
q = deque()

N = int(input())
arr = list([] for i in range(N))
for i in range(N):
    arr[i] = list(map(int, input().split()))

# 우, 하 방향만 간다고 해도 겹칠 수 있음
# visited를 써보자
res = 'Hing'
visited = list([0] * N for i in range(N))

def my_search(r, c):
    global res

    # 범위 넘거나 이동거리가 0이거나 방문했으면 컷
    if r < 0 or r >= N or c < 0 or c >= N or arr[r][c] == 0 or visited[r][c] == 1:
        return

    d = arr[r][c]  # 이동 가능 거리
    visited[r][c] = 1  # 방문 표시

    # 도착하면 결과 저장 후 컷
    if d == -1:
        res = 'HaruHaru'
        return

    # 도착 지점 조합해서 다시 탐색
    my_search(r + d, c)
    my_search(r, c + d)


my_search(0, 0)
print(res)
