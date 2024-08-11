from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

used = [0] * (max(arr)+1)

l = r = 0
res = 0
while r < N:
    if used[arr[r]] < K:
        used[arr[r]] += 1
        r += 1
    else:
        used[arr[l]] -= 1
        l += 1
    res = max(res, r - l)

print(res)