from sys import stdin

input = stdin.readline

N = int(input())  # 3 ~ 5000
arr = list(map(int, input().split()))  # -10억 ~ 10억
arr.sort()

# 절댓값이 가장 작은 쪽으로 갱신(값으로 확인하고 용액들 갱신)
min_v = int(1e9 * 3)
isFound = False
res = []

# 검색했습니다...
for i in range(N-2):
    if isFound:
        break
    refer = arr[i]
    l_p = i+1
    r_p = N-1
    while l_p < r_p:
        tmp = refer + arr[l_p] + arr[r_p]
        if abs(min_v) > abs(tmp):
            min_v = tmp
            res = [refer, arr[l_p], arr[r_p]]
        if tmp < 0:
            l_p += 1
        elif tmp > 0:
            r_p -= 1
        else:
            isFound = True
            break

print(*res)