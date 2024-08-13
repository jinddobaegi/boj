from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
coins = []

for _ in range(N):
    c = int(input())
    if c <= K:
        coins.append(c)

idx = len(coins) - 1

# 그리디
# 1) 동전들은 첫 번째 동전 가치의 배수가 되는 가치를 가짐
# 2) 각 동전은 개수 제한이 없다

cnt = 0
while K > 0:
    coin = coins[idx]
    cnt += K // coin
    K %= coin
    idx -= 1

print(cnt)