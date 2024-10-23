from sys import stdin

input = stdin.readline

# 예산 총액 내에서
# 상한선 정했을 때 가능한 최대의 총 예산 배정

n = int(input())  # 지방 수
arr = tuple(map(int, input().split()))  # 각 지방 요청 예산
total = int(input())  # 총 예산

def solution(n, arr, total):
    # 산정 필요 x
    if sum(arr) <= total:
        return max(arr)
    
    # 상한액 산정
    s, e = 1, max(arr)
    max_v = 0
    while s <= e:
        m = (s+e)//2  # 확인해볼 상한액
        tmp = total
        for x in arr:
            tmp -= min(x, m)
            if tmp < 0:  # 불가능한 경우 상한액 줄여야 함
                e = m-1
                break
        else:  # 가능한 경우 상한액 늘려야 함
            max_v = max(max_v, m)
            s = m+1

    return max_v


print(solution(n, arr, total))