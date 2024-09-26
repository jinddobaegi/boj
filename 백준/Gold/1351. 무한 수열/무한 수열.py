from sys import stdin

input = stdin.readline

def solution(i):
    if not arr.get(i):
        arr[i] = solution(i//P) + solution(i//Q)
    return arr[i]


N, P, Q = map(int, input().split())
arr = dict()
arr[0] = 1

print(solution(N))