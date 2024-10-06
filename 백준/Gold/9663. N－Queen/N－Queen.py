from sys import stdin

input = stdin.readline

N = int(input())


def solution(n):
    global res
    if n == N:
        res += 1
        return

    else:
        for i in range(N):
            if v1[i] == 0 and v2[n+i] == 0 and v3[n-i] == 0:
                v1[i] = v2[n+i] = v3[n-i] = 1
                solution(n+1)
                v1[i] = v2[n+i] = v3[n-i] = 0


res = 0
v1 = [0] * N
v2 = [0] * (N*2)
v3 = [0] * (N*2)
solution(0)
print(res)