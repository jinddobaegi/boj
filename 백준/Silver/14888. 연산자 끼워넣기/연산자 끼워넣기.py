from sys import stdin

input = stdin.readline

N = int(input())
arr = tuple(map(int, input().split()))
ops = list(map(int, input().split()))  # +, -, *, // 개수

def solution(i, res, a, s, m, d):
    global max_v, min_v

    if i == N:
        max_v = max(max_v, res)
        min_v = min(min_v, res)
        return

    if a:
        solution(i + 1, res + arr[i], a - 1, s, m, d)
    if s:
        solution(i + 1, res - arr[i], a, s-1, m, d)
    if m:
        solution(i + 1, res * arr[i], a, s, m-1, d)
    if d:
        solution(i + 1, int(res / arr[i]), a, s, m, d-1)


min_v = int(1e9)
max_v = int(-1e9)
# solution(1, arr[0])
solution(1, arr[0], *ops)
print(max_v)
print(min_v)