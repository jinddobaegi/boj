from sys import stdin

input = stdin.readline

H, W = map(int, input().split())
blocks = tuple(map(int, input().split()))
res = 0
for i in range(1, W-1):
    # 자신을 기준으로 양쪽에서 제일 높은 블록 확인
    l_max = max(blocks[:i])
    r_max = max(blocks[i+1:])

    standard = min(l_max, r_max)  # 둘 중 낮은 애 확인

    # 그게 자기보다 높은지 확인
    if standard > blocks[i]:
        res += standard - blocks[i]

print(res)