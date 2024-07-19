from sys import stdin
input = stdin.readline
N = int(input())
flag = True
prev_lv = 0
stack = []
res = [0] * N
for i in range(N):
    current_lv = int(input())
    if current_lv > prev_lv+1:
        flag = False
        res = [-1]
        break
    prev_lv = current_lv
    while stack and stack[-1][1] >= current_lv: stack.pop()
    if stack: res[stack[-1][0]] += 1
    stack.append((i, current_lv))
for cnt in res: print(cnt)