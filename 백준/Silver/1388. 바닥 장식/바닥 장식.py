from collections import deque

# 나무 판자 너비는 1 고정
# 방은 직사각형
# 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다..?
# 뭔 말을 이렇게 하냐 ㅋㅋ

# 그냥 한 칸이 정사각형인데
# 판자를 세로로 놓은 건지 가로로 놓은 건지 판단하면 될 듯

# N: 방 세로 길이
# M: 방 가로 길이

# 가로로 순회하면서 '-'
# 세로로 순회하면서 '|'
# 이어진 거 확인하면 될 듯

N, M = map(int, input().split())
arr = list(list() for _ in range(N))

for i in range(N):
    arr[i] = list(input())


# 행 방향 순회
cnt = 0

# 다르다는 정보만 남겨서, '-' 개수만 셀 것임
for r in range(N):
    tmp_list = deque()
    tmp_list.append(arr[r][0])  # 모든 행의 첫 열은 넣고 시작

    for c in range(1, M):
        if arr[r][c-1] != arr[r][c]:
            tmp_list.append(arr[r][c])

    cnt += tmp_list.count('-')

# 열 방향 순회, 위와 동일하게
for c in range(M):
    tmp_list = deque()
    tmp_list.append(arr[0][c])  # 모든 열의 첫 행은 넣고 시작

    for r in range(1, N):
        if arr[r-1][c] != arr[r][c]:
            tmp_list.append(arr[r][c])

    cnt += tmp_list.count('|')

print(cnt)