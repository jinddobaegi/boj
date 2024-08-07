from sys import stdin

input = stdin.readline


def flip(r, c):
    if not (0 <= r <= N-3 and 0 <= c <= M-3):
        return

    for i in range(3):
        nr = r + i
        for j in range(3):
            nc = c + j
            if A[nr][nc]:
                A[nr][nc] -= 1
            else:
                A[nr][nc] += 1


N, M = map(int, input().split())
A = list(list(map(int, list(input().rstrip()))) for _ in range(N))
B = list(list(map(int, list(input().rstrip()))) for _ in range(N))

res = 0
if (N < 3 or M < 3) and (A != B):
    res = -1
else:
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                flip(i, j)
                res += 1

print(res if A==B else -1)