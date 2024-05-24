from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
stack = deque()

# 막대를 하나씩 살펴볼건데
# 이전보다 낮아지는 순간이 오면
# 그 막대는 다음 최소 높이가 되어야 함
# 따라서 그 이전 막대 idx를 끝으로
# 왼쪽 막대 높이들을 살펴보자
# 어차피 낮아지거나 같을 것임

max_v = 0

for i in range(N):
    h = int(input())
    left_idx = i
    while stack and stack[-1][1] > h:
        left_idx, left_h = stack.pop()
        # 왼쪽 막대 높이 기준으로 계산
        max_v = max((i-left_idx) * left_h, max_v)
        # 원래는 가로 길이가
        # (i-1) - left_idx + 1인데 정리됨

    stack.append((left_idx, h))

while stack:
    idx, h = stack.pop()
    max_v = max(max_v, (N-idx)*h)

print(max_v)