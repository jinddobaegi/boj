from sys import stdin

input = stdin.readline

# 연산자의 우선순위를 무시하고 앞에서부터 진행
# 나눗셈은 나머지 버림
# 음수를 양수로 나눌 땐 양수로 바꿔 나눈 뒤 몫에 부호를 붙임
# 결과의 최대, 최솟값을 구하자

N = int(input())
arr = tuple(map(int, input().split()))
ops = list(map(int, input().split()))  # +, -, *, // 개수


# 백트래킹 써보자

# 이거 왜 안되지????
# def solution(i, res):  # 초기화값 i = 1, res = arr[0]
#     global max_v, min_v
#
#     if i == N:
#         max_v = max(max_v, res)
#         min_v = min(min_v, res)
#         return
#
#     x = arr[i]  # 현재 숫자
#     for j in range(4):
#         if ops[j]:  # 해당 부호 사용 가능한 경우
#             # 해당 부호 사용하는 경우
#             ops[j] -= 1
#             if j == 0:
#                 solution(i+1, res + x)
#             elif j == 1:
#                 solution(i+1, res - x)
#             elif j == 2:
#                 solution(i+1, res * x)
#             else:
#                 if res == 0:  # ZeroDivisionError 피하기 위해
#                     ops[j] += 1
#                     continue
#
#                 if res < 0:
#                     res = -(-res // x)
#                 else:
#                     res //= x
#                 solution(i+1, res)
#
#             # 해당 부호 사용 취소, 다음 for문 확인 == 사용 안하는 경우
#             ops[j] += 1


def solution(i, res, a, s, m, d):
    global max_v, min_v

    if i == N:
        max_v = max(max_v, res)
        min_v = min(min_v, res)

    if a:
        solution(i + 1, res + arr[i], a - 1, s, m, d)
    if s:
        solution(i + 1, res - arr[i], a, s-1, m, d)
    if m:
        solution(i + 1, res * arr[i], a, s, m-1, d)
    if d:
        solution(i + 1, int(res / arr[i]), a, s, m, d-1)


min_v = int(1e9)
max_v = int(-1e9)
# solution(1, arr[0])
solution(1, arr[0], ops[0], ops[1], ops[2], ops[3])
print(max_v)
print(min_v)