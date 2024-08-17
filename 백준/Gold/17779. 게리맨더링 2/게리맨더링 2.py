from sys import stdin
from pprint import pprint

input = stdin.readline

# 격자 크기: N x N
# 다섯 개 선거구로 나눠야 함
# 한 선거구 안에 있는 지역은 연결돼있어야 함

# 5번을 정하면 나머지는 정해짐

# 한 거점 정하기 => 5번의 최상단
# 경계의 길이는 최소 1이고 그때도 다섯 칸은 차지함(예시 그림 3) => 5번

# 그렇다면 (0, 0)부터 거점 돌면서
# d1과 d2의 모든 조합을 구하고 확인하는 수 밖에 없다
# r은 0 이상, N-2 "미만" 가능
# c는 0과 N-1은 안됨


def make_border_of_fifth(r, c, d1, d2, area):
    for i in range(d1):
        area[r+i][c-i] = 5
    for i in range(1, d2+1):
        area[r+i][c+i] = 5
    for i in range(1, d1+1):
        area[r+d2+i][c+d2-i] = 5
    for i in range(d2+1):
        area[r+d1+i][c-d1+i] = 5


def fill_in_fifth(r, d1, d2, area):
    flag = False
    for i in range(r+1, r+d1+d2):
        for j in range(N):
            if area[i][j] == 5:
                flag = 1 - flag
                continue

            if flag:
                area[i][j] = 5


def update_min(r, c, d1, d2):
    global min_v

    area = [[0] * N for _ in range(N)]

    # 5구역 표시
    area[r][c] = 5
    make_border_of_fifth(r, c, d1, d2, area)
    # fill_in_fifth(r, d1, d2, area)
    # pprint(area)
    flag = False
    counts = [0] * 5
    for i in range(N):
        for j in range(N):
            if area[i][j] == 5:  # 5구역 경계 만나면
                counts[4] += populations[i][j]  # 5구역 인구 추가
                if r < i <= r+d1+d2-1:  # 꼭짓점 아니면 flag on/off
                    flag = 1 - flag
            elif flag:  # 경계 안쪽 5구역이면
                counts[4] += populations[i][j]  # 5구역 인구 추가
                # 디버깅용
                area[i][j] = 5
            # 1구역: 5번보다 r,c 다 작음
            elif i < r+d1 and j <= c:
                counts[0] += populations[i][j]
                # 디버깅용
                area[i][j] = 1
            # 2구역: 5번보다 r은 작고, c는 큼
            elif i <= r+d2 and j > c:
                counts[1] += populations[i][j]
                # 디버깅용
                area[i][j] = 2
            # 3구역: 5번보다 r은 크고, c는 작음
            elif i >= r+d1 and j < c-d1+d2:
                counts[2] += populations[i][j]
                # 디버깅용
                area[i][j] = 3
            # 4구역: 5번보다 r,c 다 큼
            else:
                counts[3] += populations[i][j]
                # 디버깅용
                area[i][j] = 4
                
    # print(counts)
    # pprint(area)
    tmp = max(counts) - min(counts)
    min_v = min(min_v, tmp)


N = int(input())
populations = list(list(map(int, input().split())) for _ in range(N))
min_v = int(1e9)
# 1) 거점 순회
for r in range(N-2):
    for c in range(1, N-2):
        for d1 in range(1, N-2):
            if r+d1 >= N or c-d1 < 0:  # 범위확인
                break
            for d2 in range(1, N-2):
                if r+d1+d2 >= N or c+d2 >= N:  # 범위확인
                    break
                update_min(r, c, d1, d2)

print(min_v)

# update_min(1, 4, 3, 2)