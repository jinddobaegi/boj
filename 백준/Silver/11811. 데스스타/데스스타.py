from sys import stdin

input = stdin.readline

# 길이 N의 수열 ai가 필요 -> 없음
# 쪽지에 수열이 만족해야 하는 조건이 있음
# 길이 N의 정방행렬 있음
# 행렬의 aij는, 수열의 ai와 aj에 비트연산 and 수행한 결과값임
# axx는 못 읽음

# 예를 들어 수열이 [1, 2, 1, 3, 0, 5]이었다면
# arr[1][2] = seq[1] & seq[2]라는 뜻임
# 그래서 arr[2][1]도 똑같음
# arr[x][x]는 즉 수열 그 자체임

# 그러면 내가 seq[i]를 구하려면
# arr[i]의 원소들을 전부 비트연산 or로 더해주자
# 결과로 나온 값(사실 얘가 결국 seq[i]임)과 seq의 원소들을 각각 and 연산 해주면
# arr[i]의 원소들의 값과 일치할 것이다

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
seq = [0] * N

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        seq[i] |= arr[i][j]

print(*seq)