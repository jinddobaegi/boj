from sys import stdin

input = stdin.readline

N = int(input())


def check_pattern(s_len, num_str):
    for x in range(s_len-1):  # 절반 나눴을 때 앞 문자열 비교 시작점
        for y in range(1, s_len//2+1):  # 비교할 패턴의 길이
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