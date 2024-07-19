from sys import stdin

input = stdin.readline

N = int(input())
stack = []

for _ in range(N):
    input_v = tuple(map(int, input().split()))
    if len(input_v) == 2:
        stack.append(input_v[1])
        continue
    else:
        x = input_v[0]

    if x == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif x == 3:
        print(len(stack))
    elif x == 4:
        print(0 if stack else 1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)