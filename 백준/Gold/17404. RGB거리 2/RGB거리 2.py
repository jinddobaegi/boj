# 처음엔 0, N-1번째 집 빼고 진행한 다음
# N-1번째에 선택하는 색깔에 따라
# 0번째 집과, 나머지 중간 집들을 선택하려 했음
# 근데 틀림

# 그래서 블로그 글 참고했음 ㅜ
# 1번 집을 고정하고 돌도록 하면 된다고 함

from sys import stdin

input = stdin.readline

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))

# 첫 번째 집을 일단 최댓값으로 초기화
max_v = 1001
dp = list([0]*3 for _ in range(N))

# 첫 번째 집을 하나씩 정하고
# 그때의 최솟값을 저장
res = []
for init_color in range(3):
    # First Color Init
    dp[0][0] = dp[0][1] = dp[0][2] = max_v
    dp[0][init_color] = arr[0][init_color]

    # DP
    for i in range(1, N):
        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[i][2] + min(dp[i-1][1], dp[i-1][0])

    tmp = int(1e7)
    for j in range(3):
        if j == init_color:
            continue

        if tmp > dp[N-1][j]:
            tmp = dp[N-1][j]

    res.append(tmp)

print(min(res))