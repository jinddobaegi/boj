import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b, c = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

# 특정 구간의 흐림 정도의 합 계산하는 리스트
sum_lst = [[0] for _ in range(n)]

# 각 행
for i, row in enumerate(area):
    # 각 열 돌면서
    for j, col in enumerate(row):
        # 현재까지 계산된 누적합의 마지막 값에 현재 값 더해서 추가해주기
        sum_lst[i].append(sum_lst[i][-1] + col)

# 최소 흐림 정도 합
ans = sys.maxsize   # 최댓값 설정에 이런것도 있더라구요

# 차 왼쪽 / 캠핑카 오른쪽
def check_one(x, y):
    # 배치 가능한지 먼저 확인
    # 땅을 벗어나는 경우
    if (y + b + c > m) or (x + a > n):
        # 배치가 불가능하면 겁나 큰 값 반환하기 (이 위치 선택 안 되게)
        return sys.maxsize
    # 흐림 정도 합 초기화
    val = 0


    # 차랑 캠핑카 배치될 수 잇는 모든 행에 대해서 반복해주는거
    for i in range(x, x+a):
        # 현재 행에서  y ~ y+b+c까지 흐림 정도 합 계산
        val += sum_lst[i][y + b + c] - sum_lst[i][y]

    return val

# 차 위쪽 / 캠핑카 아래쪽
def check_two(x, y):
    # 땅 벗어나는 경우
    if (y + c+ a > m) or (x+a+b > n):
        return sys.maxsize
    val = 0

    for i in range(x, x+a):
        # y ~ y+c 까지 더해
        val += sum_lst[i][y+c] - sum_lst[i][y]

    # 캠핑카가 시작한는 위치
    hx, hy = x+a, y+c

    # 캠핑카가 배치될 수 있는 모든 행에 대해서 반복
    for i in range(hx, hx+b):
        # hy ~ hy+a 까지 더해
        val += sum_lst[i][hy+a] - sum_lst[i][hy]

    return val


# 캠핑카 왼쪽 / 차 오른쪽
def check_three(x, y):
    if (y + b + a > m) or (x + a + c > n):
        return sys.maxsize
    val = 0

    for i in range(x, x + a):
        val += sum_lst[i][y + b] - sum_lst[i][y]
    hx, hy = x + a, y + b

    for i in range(hx, hx + c):
        val += sum_lst[i][hy + a] - sum_lst[i][hy]

    return val



# 가능한 모든 위치 다 탐색해서
# 최솟값 갱신하자
for i, row in enumerate(area):
    for j, col in enumerate(row):
        ans = min(ans, check_one(i, j))
        ans = min(ans, check_two(i, j))
        ans = min(ans, check_three(i, j))

print(ans)