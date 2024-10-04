from sys import stdin

input = stdin.readline

N = int(input())

# 길이가 N인 수열 만들 것
# 동일한 부분수열이 인접해있으면 안됨
# 이어 붙여 하나의 정수로 보았을 때 가능한 N자리 수 중 가장 작도록

# 일단 각 숫자의 이전 자리를 파악해야
# 같은 숫자가 나왔을 때 패턴을 찾을 수 있을 것 같음

# 1) 재귀함수로 수열을 만들어 나가면서
# 2) 패턴 체크
# 3) N의 길이가 완성되면 컷


def check_pattern(s_len, num_str):
    for x in range(s_len-1):  # 절반 나눠서 앞 부분 비교 시작점
        for y in range(1, s_len//2+1):  # 비교할 패턴의 길이
            if x+y+y > s_len:  # 뒷 부분 끝 점이 범위를 넘어가는지 확인
                break
            if num_str[x:x+y] == num_str[x+y:x+y+y]:
                return False
    return True


def solution(i, num_str):
    if i == N:
        print(num_str)
        exit()

    for x in '123':  # 123 순으로 숫자를 붙이기 때문에 최솟값을 보장받음
        if check_pattern(i+1, num_str + x):
            solution(i+1, num_str + x)


solution(1, '1')