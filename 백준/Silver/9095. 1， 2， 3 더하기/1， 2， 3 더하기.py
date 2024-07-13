from sys import stdin

input = stdin.readline
T = int(input())

# 순서도 중요함
# 1: 1
# 2: 2, 11
# 3: 3, 21, 12, 111
# 4 이후로 a+1, b+2, c+3의 형태로 나타내면
# a는 k-1, b는 k-2, c는 k-3이 됨

dp = [0] * 12  # 0 안 쓸 거임
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    print(dp[int(input())])
