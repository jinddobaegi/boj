from sys import stdin

input = stdin.readline

# 1) 선행 작업이 있다면 그것들을 먼저 끝내야 한다
# 2) 특정 작업 i의 선행 작업 번호는 항상 i 미만이다
# 3) 선행 관계가 없다면 동시 작업이 가능하다!

# 작업 완료에 필요한 최소 시간을 구하라

N = int(input())
durations = [0] * (N+1)
prior_works = [[] for _ in range(N+1)]
dp = [0] * (N+1)

for i in range(1, N+1):
    d, n_of_p, *p_of_i = map(int, input().split())
    durations[i] = d
    if n_of_p:
        p_of_i.sort(reverse=True)  # 선행작업 내림차순 정렬
        prior_works[i] = p_of_i

# 번호가 클 수록 선행 작업이 많을 가능성이 크니까
# 맨 끝 작업부터 시간이 얼마나 걸리는지 계산하자
# 선행 작업의 시간까지 포함하여 계산하기 위해 재귀함수를 사용해보자
# 만약 해당 작업을 하기 위해 걸리는 시간이 기존 res보다 길면 update


def solution(w):
    if not dp[w]:
        dp[w] = durations[w]  # w의 작업시간

        # 선행 작업 있는 경우
        if prior_works[w]:
            tmp = 0
            for p in prior_works[w]:  # 선행 작업
                # 그 중 가장 시간이 오래 걸리는 것(선행 작업도 동시에 할 수 있으니까)
                tmp = max(tmp, solution(p))
            dp[w] += tmp  # w와 선행 작업을 모두 했을 때 걸리는 시간

    return dp[w]


res = 0
for i in range(N, 0, -1):
    if not dp[i]:
        res = max(res, solution(i))

print(res)