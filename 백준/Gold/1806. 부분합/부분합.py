from sys import stdin

input = stdin.readline

N, S = map(int, input().split())
arr = tuple(map(int, input().split()))
INF = int(1e9)


def solution():
    res = INF
    l = r = 0
    tmp_s = arr[l]

    while l < N:
        if tmp_s >= S:
            res = min(res, r-l+1)
            tmp_s -= arr[l]
            l += 1
        else:
            if r == N-1:
                break
            r += 1
            tmp_s += arr[r]

    if res == INF:
        res = 0

    return res


print(solution())