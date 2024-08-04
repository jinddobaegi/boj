from sys import stdin

input = stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    arr = [0] + list(map(int, input().split()))
    dp = [[0] * (K+1) for _ in range(K+1)]
    cumsum = [0]
    for i in range(1, K+1):
        cumsum.append(cumsum[-1] + arr[i])  # 누적합 배열 만드는 코드
    
    for gap in range(1, K):  # 간격: 1 ~ K-1
        for s in range(1, K - gap + 1):
            e = s + gap
            min_v = int(1e9)
            for p in range(s, e):
                min_v = min(min_v, dp[s][p] + dp[p+1][e])
            dp[s][e] = min_v + (cumsum[e] - cumsum[s-1])

    print(dp[1][K])