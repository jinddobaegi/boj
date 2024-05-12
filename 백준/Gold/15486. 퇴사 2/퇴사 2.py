from sys import stdin

input = stdin.readline


N = int(input())

t_list = [0] * (N+1)
p_list = [0] * (N+1)

for i in range(1, N+1):
    t, p = map(int, input().split())
    t_list[i] = t
    p_list[i] = p

dp = [0] * (N+1)

for date in range(1, N+1):
    # 오늘을 기준으로 두 가지 작업을 수행해야 함
    # 1) 어제까지 계산된 최댓값(어제 계산된 어제의 최댓값)과
    #    미리 계산된 오늘의 값(이전의 어느 시점에 저장된 값) 중
    #    최댓값으로 오늘까지 벌 수 있는 돈을 갱신해야함
    dp[date] = max(dp[date], dp[date-1])

    # 2) 그리고 오늘 시작하는 일이 끝나는 날에 대해서도 똑같은 일을 해야 함
    end_date = date + t_list[date] - 1
    #    그날에 저장되어있는 값(오늘 일을 선택하지 않은 경우)과
    #    오늘까지의 값 + 오늘 일 선택했을 때의 값 중
    #    최댓값으로 그날 벌 수 있는 돈을 갱신
    if end_date <= N:
        dp[end_date] = max(dp[end_date], dp[date-1] + p_list[date])

print(max(dp))