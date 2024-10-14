from sys import stdin

input = stdin.readline

N, H = map(int, input().split())  # 동굴 길이와 높이

# 아래 위 번갈아가면서
down = [0] * (H+1)
up = [0] * (H+1)
for i in range(N):
    x = int(input())
    if i % 2 == 0:  # 아래
        down[x] += 1
    else:  # 위
        up[x] += 1

# 지나는 높이가 3인 경우
# down은 3 이상의 것들을 확인해야 함
# up은 8 이상의 것들을 확인해야 함

# 누적합 생성
for i in range(H, 0, -1):
    down[i-1] += down[i]
    up[i-1] += up[i]

min_v = N
cnt = 0
for fly_h in range(1, H+1):
    tmp = down[fly_h] + up[H-fly_h+1]
    if min_v > tmp:
        min_v = tmp
        cnt = 1
    elif min_v == tmp:
        cnt += 1

print(min_v, cnt)
