from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))

# 0번 idx는 사용 x
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# Clouds Init
clouds = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

for _ in range(M):
    d, s = map(int, input().split())

    new_clouds = set()  # 이동한 구름 위치 담을 것임

    # 구름마다 확인
    while clouds:
        cloud_r, cloud_c = clouds.pop()

        # directions에 있는 방향들로 이동
        nr = cloud_r + (dr[d] * s)
        nc = cloud_c + (dc[d] * s)

        # 범위 안에 오도록 좌표 수정
        while nr < 0:
            nr += N
        nr %= N  # N으로 나눈 나머지

        while nc < 0:
            nc += N
        nc %= N

        # 바구니에 물 붓기, 이동한 위치 저장
        arr[nr][nc] += 1
        new_clouds.add((nr, nc))

    # 구름 옮기고 물 다 부은 상태
    # 경계 내 대각선 체크 후 물 복사 <- 구름 다 돌고 확인해야 함
    for tmp_r, tmp_c in new_clouds:

        # 대각 바구니 확인
        for diag_dr, diag_dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            tmp_nr = tmp_r + diag_dr
            tmp_nc = tmp_c + diag_dc

            if 0 <= tmp_nr < N and 0 <= tmp_nc < N and arr[tmp_nr][tmp_nc]:
                arr[tmp_r][tmp_c] += 1

    # 이동한 이전 구름 제외한 위치에 물 2 이상 있는지 체크
    for tr in range(N):
        for tc in range(N):
            if arr[tr][tc] >= 2 and (tr, tc) not in new_clouds:
                # 구름 생기고 물 양 2씩 감소
                clouds.append((tr, tc))
                arr[tr][tc] -= 2

res = 0
for r in range(N):
    for c in range(N):
        res += arr[r][c]

print(res)
