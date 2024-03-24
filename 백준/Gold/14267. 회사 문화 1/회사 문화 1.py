# 직속 부하 내리 칭찬?!
# 각자 얼마의 칭찬을 받았는지 출력

from sys import stdin

input = stdin.readline

# n: 직원
# m: 칭찬의 횟수
n, m = map(int, input().split())

# 부하를 인덱스로 상사를 값으로
par = [0] + list(map(int, input().split()))
implements = [0] * n

for _ in range(m):
    # i: 칭찬 "받은" 직원 번호
    # w: 칭찬 수치
    i, w = map(int, input().split())
    implements[i-1] += w

for c in range(3, n+1):
    p = par[c]
    # 3번부터 자기꺼에 부모꺼 더하면 됨
    implements[c-1] += implements[p-1]

print(*implements, sep=' ')