from sys import stdin
from itertools import permutations

input = stdin.readline

N = int(input())
result = tuple(tuple(map(int, input().split())) for _ in range(N))

# 문제
# result에는 i번째 이닝에 j 타자의 결과가 정해져 있다
# 0번 선수 => 4번 타자 고정

P = (x for x in range(1, 9))
R = 0
for line_up in permutations(P):
    line_up = list(line_up)
    line_up = tuple(line_up[:3] + [0] + line_up[3:])

    tmp_R = 0  # 라인업 점수
    turn = 0   # 차례
    for i in range(N):    # 이닝
        out_cnt = 0       # 아웃카운트
        b1 = b2 = b3 = 0  # 베이스 주자 유무
        while out_cnt != 3:
            j = line_up[turn]       # 이번 타자
            hit_res = result[i][j]  # 타자의 결과

            if hit_res == 0:
                out_cnt += 1

            elif hit_res == 1:
                tmp_R += b3
                b3, b2, b1 = b2, b1, 1

            elif hit_res == 2:
                tmp_R += b3 + b2
                b3, b2, b1 = b1, 1, 0

            elif hit_res == 3:
                tmp_R += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0

            else:
                tmp_R += b3 + b2 + b1 + 1
                b1 = b2 = b3 = 0

            turn += 1
            if turn == 9:
                turn = 0

    R = max(R, tmp_R)

print(R)