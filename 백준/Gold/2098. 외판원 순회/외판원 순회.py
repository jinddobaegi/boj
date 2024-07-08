# 입력값 초기화 & 배열 설정
N = int(input())
W = [[] for _ in range(N)]
dp = [[0 for _ in range(1 << N - 1)] for _ in range(N)]

for i in range(N):
    W[i] = list(map(int, input().split()))


# 현재 위치 i, 지금까지 방문한 도시들의 집합 route일 때 최소 비용 구하는 함수
def solution(i, route):
    global N, W, dp

    # 이미 방문한 경로면 memoization 해둔 값이므로 return
    if dp[i][route] != 0:
        return dp[i][route]

    # 모든 도시를 다 방문한 경우
    if route == (1 << (N - 1)) - 1:
        # 마지막 위치에서 0번 도시로 가는 경로가 없는 경우
        if not W[i][0]:
            return float('inf')
        # 마지막 위치에서 0번 도시로 가는 경로가 있는 경우 정답 반환
        else:
            return W[i][0]

    # 점화식을 토대로, 최소값을 찾아서 다음 방문 도시 선택하기
    min_price = float('inf')
    for j in range(1, N):
        # i번째 도시에서 j번째 도시로 가는 경로가 없는 경우
        if not W[i][j]:
            continue
        # j번째 도시가 이미 방문한 도시인 경우
        if route & (1 << j - 1):
            continue
        # j번째 도시를 방문했을 경우 비용 계산해서 최소값이면 선택
        # i -> j 도시 가는 비용 + solution(j번째 도시, j번째 도시를 추가한 경로)
        dist = W[i][j] + solution(j, route | (1 << (j - 1)))
        if min_price > dist:
            min_price = dist
    dp[i][route] = min_price
    return min_price


# 0번째 도시에서 출발, 아무 도시도 방문하기 않았기 때문에 0
print(solution(0, 0))