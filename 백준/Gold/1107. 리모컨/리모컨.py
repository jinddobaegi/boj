from sys import stdin
from collections import deque

input = stdin.readline

# 채널은 0과 양의 정수, 무한개
# 시작은 100, N까지 이동해야 함
# 고장난 버튼이 주어졌을 때, N까지 이동하기 위한 최소 클릭 수

N = int(input())  # 50만 이하
M = int(input())  # 10 이하
buttons = '+-1234567890'
if M:
    buttons = ''
    tmp = tuple(map(str, input().split()))  # 0~9, +, - 있을 수 있음
    for x in '+-1234567890':
        if x not in tmp:
            buttons += x

# print(buttons)
# bfs?
# 일단 해보자 ㅋㅋ
res = 0
if N != 100:
    q = deque()
    visited = set()
    q.append((100, 0, 0))  # (채널, 이전에 숫자 눌렀는지, cnt)
    visited.add((100, 0))  # (채널, 이전에 숫자 눌렀는지)
    is_found = False
    is_num = 0
    while q:
        # print(q)
        ch, is_num_before, cnt = q.popleft()
        #############  RES TEST  #############
        res = cnt+1
        #############  RES TEST  #############
        for b in buttons:
            if b == '+':
                is_num = 0
                n_ch = ch + 1
            elif b == '-':
                is_num = 0
                n_ch = ch - 1
            elif is_num_before:  # 숫자 버튼인데 이전에 누른 게 숫자였던 경우
                is_num = 1
                n_ch = int(str(ch) + b)
            else:  # 숫자 버튼인데 이전에 누른 게 숫자가 아닌 경우
                is_num = 1
                n_ch = int(b)
            if 0 <= n_ch <= 1000000 and (n_ch, is_num) not in visited:
                # print(f'현재채널: {ch}, 이전숫자: {is_num_before} 누른버튼: {b}, 새채널: {n_ch}')
                if n_ch == N:
                    is_found = True
                    break
                q.append((n_ch, is_num, res))
                visited.add((n_ch, is_num))

        if is_found:
            break

print(res)