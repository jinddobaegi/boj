# 우리가 1차원 배열
# N개의 얼음 양동이 좌표 x들이 주어짐
# 각 좌표에는 g씩의 얼음이 들어있음
# 곰 이동거리 K

from sys import stdin

input = stdin.readline


N, K = map(int, input().split())

arr = [0] * 1000001

for _ in range(N):
    g, x = map(int, input().split())
    arr[x] = g

s = 0
if K >= 500000:
    e = 1000000
else:
    e = 2 * K

max_v = 0
for i in range(e+1):
    if arr[i] > 0:
        max_v += arr[i]

tmp = max_v

for j in range(e+1, 1000001):
    tmp -= arr[j-(e+1)]
    tmp += arr[j]
    if max_v < tmp:
        max_v = tmp

print(max_v)
