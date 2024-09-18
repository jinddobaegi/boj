from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

# C개의 공유기를 집들에 설치할 것임
# 공유기를 설치했을 때 가장 인접한 공유기 간 거리를 최대로 해야 함

N, C = map(int, input().split())
homes = list(int(input()) for _ in range(N))
homes.sort()

# 블로그 참고ㅜ
# 이분탐색을 쓰는데, 어떤 지점을 찾는 게 아닌
# 공유기 사이의 거리를 찾는 데에 이분탐색을 쓴다?

s = 1  # 공유기 간 최소 거리
e = homes[N-1] - homes[0]  # 공유기 간 최대 거리
res = 0  # update할 공유기 간 최소 거리

while s <= e:
    m = (s+e)//2  # 현재 설정한 공유기 간 거리
    cur = homes[0]  # 0번째 집에 설치하고 시작
    cnt = 1  # 설치 공유기 대수
    
    # 현재 거리가 m일 때
    for i in range(1, N):
        # 공유기를 돌면서, 이전 공유기부터 정해놓은 거리 이상?
        if homes[i] >= cur + m:
            # 설치
            cnt += 1
            cur = homes[i]

    # 가능한 수보다 적게 설치?
    if cnt < C:
        # 공유기 간 거리를 줄여야 함
        e = m-1
    # 가능한 수 이상으로 설치?
    else:
        # 저장하고, 공유기 간 거리 늘려보자
        res = m
        s = m+1

print(res)