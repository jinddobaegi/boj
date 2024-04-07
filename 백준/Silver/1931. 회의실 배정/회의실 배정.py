from sys import stdin

input = stdin.readline

# 시작, 끝나는 시간 주어짐(동일할 수 있음)
# 각 회의가 겹치지 않게 하면서 회의실 사용할 수 있는 회의 최대 수

'''
"다시보기 - 활동 선택 문제" 참고함
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

'''

# N: 회의의 수
# N줄만큼 시작, 끝 시간 주어짐

# 완탐으로 부분집합을 만들면 너무 많아짐
# 1) 종료 시간 순으로 활동들을 정렬
# 2) 종료 시간이 가장 빠른 활동을 선택
#       - 그 활동의 시작 시간이 앞선 활동의 종료 시간보다 빠르지 않은지 확인
# 3) 그럼 그 종료 시간부터 다시 1,2 반복
#       - 또 종료 시간이 가장 빠른 활동을 선택

# 재귀 알고리즘

N = int(input())
meetings = list(list(map(int, input().split())) for _ in range(N))
meetings.sort(key=lambda x: (x[1], x[0]))
meetings = [[0, 0]] + meetings

res = []
j = 0  # 이전 회의

for i in range(1, N+1):
    if meetings[i][0] >= meetings[j][1]:
        res.append(i)
        j = i

print(len(res))
