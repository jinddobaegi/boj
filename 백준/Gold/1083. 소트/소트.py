from sys import stdin

input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
S = int(input())


def solution(s):
    d = 0  # 정렬된 숫자 개수
    while s > 0 and d != N:
        # 정렬된 숫자들 제외하고
        # 앞에서부터 S+1개 중 가장 큰 수를 맨 앞으로
        x = max(arr[d:min(d+s+1, N)])  # S가 엄청 큰 경우 대비
        x_idx = arr.index(x)
        for i in range(x_idx, d, -1):
            if s <= 0:
                return
            if arr[i-1] < arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                s -= 1
        d += 1


solution(S)
print(*arr)