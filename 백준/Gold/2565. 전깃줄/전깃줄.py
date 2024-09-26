from sys import stdin

input = stdin.readline

# 교차하는 전깃줄이 없도록
# 제거해야 하는 전깃줄 최소 개수

N = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(N))
arr.sort()

# dp[k]: A의 k번째까지 전깃줄까지 확인했을 때
# 가장 길게 교차가 없었던 길이를 저장할 것임
dp = [1] * N  # 기본으로 한 개씩은 가능하니까 1로 초기화

for ai in range(1, N):    # ai와 연결된 b를 확인하기 위해
    for aj in range(ai):  # ai 이전에 있는 것들 aj의 연결된 b를 확인
        if arr[aj][1] < arr[ai][1]:
            dp[ai] = max(dp[ai], dp[aj]+1)
            # aj를 돌리면서 ai를 갱신
            # 그 ai는 aj for문이 한 바퀴 돌고 나면
            # 다음 ai 차례에서 aj의 역할을 맡게 됨!

            # ai가 1, aj가 0일 때부터 확인했기 때문에
            # aj에는 이전에 ai가 돌면서 저장되었던 가능한 최대 길이가 저장되어 있음
            # ai에는 그 aj 상태에서 ai까지 이어서 더 추가할 수 있는지를 확인하는 것임!

print(N - max(dp))