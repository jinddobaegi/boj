from collections import deque

N = int(input())
cnt = 0

for i in range(N):
    stack = deque()

    sentence = input()
    for c in sentence:
        if not stack:
            stack.append(c)
        else:
            # top이 c와 같은 경우
            if stack[-1] == c:
                stack.pop()
            # top이 c와 다른 경우
            else:
                stack.append(c)
    if not stack:
        cnt += 1

print(cnt)
