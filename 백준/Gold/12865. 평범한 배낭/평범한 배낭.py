from sys import stdin
input = stdin.readline
N, K = map(int, input().split())
loadings = list(tuple(map(int, input().split())) for _ in range(N))
dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for bag_w in range(1, K+1):
        cur_loading = loadings[i-1]
        if cur_loading[0] > bag_w:
            dp[i][bag_w] = dp[i-1][bag_w]
        else:
            dp[i][bag_w] = max(dp[i-1][bag_w], cur_loading[1]+dp[i-1][bag_w - cur_loading[0]])
print(dp[N][K])