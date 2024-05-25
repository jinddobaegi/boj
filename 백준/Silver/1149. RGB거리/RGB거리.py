from sys import stdin

input = stdin.readline


N = int(input())

# RGB순
# 전후로 집색이 다르면 됨
arr = list(list(map(int, input().split())) for _ in range(N))

# DP를 2차원으로!
dp = list([0]*3 for _ in range(N))
dp[0][0], dp[0][1], dp[0][2] = arr[0][0], arr[0][1], arr[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + arr[i][2]

print(min(dp[N-1]))