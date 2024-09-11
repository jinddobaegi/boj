from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

M, N = map(int, input().split())  # 행, 열 순
arr = tuple(tuple(map(int, input().split())) for _ in range(M))


def solution(i, j):
    # 끝에 도달한 경우 => 여기서 재귀가 한 개씩 return 됨
    if i == M-1 and j == N-1:
        return 1

    if dp[i][j] == -1:
        cnt = 0
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] < arr[i][j]:
                cnt += solution(ni, nj)

        dp[i][j] = cnt

    return dp[i][j]


dp = [[-1] * N for _ in range(M)]  # dp[i][j]: (i, j)에서 도착지점에 도착하기 위한 경우의 수
print(solution(0, 0))