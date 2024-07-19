from sys import stdin

input = stdin.readline

N = int(input())
levels = [int(input()) for _ in range(N)]

flag = False
prev_lv = 0
for lv in levels:
    if lv > prev_lv+1:
        flag = True
        break
    prev_lv = lv

if flag:
    print(-1)
else:
    res = [0] * N
    stack = []
    
    # 나보다 작은 애만 남도록 해서
    # stack에 push하자
    for i in range(N):
        current_lv = levels[i]

        # 스택에 나보다 크거나 같은 애들 다 pop
        # 얘를 매번 하기 때문에 뭐 cnt 쌓고 다 더해주는 게 아니라
        # 아래 코드에서 +1만 해주면 되는 것임
        while stack and stack[-1][1] >= current_lv:
            stack.pop()

        # 스택이 안 비어있다면
        # 나보다 작은 애만 남은 상태
        if stack:
            res[stack[-1][0]] += 1

        # 위의 상태를 만들어놓고 push
        stack.append((i, current_lv))

    for cnt in res:
        print(cnt)