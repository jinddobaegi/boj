from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
a, b, c = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
min_v = int(1e9)

# a: 공통 너비
# b: 차 길이
# c: 카라반 길이

# 일자 하나, 기역자 둘
# 1) 일자
# (0, 0)에서 시작해서 첫 번째 값 구하고
# 그냥 옮기면서 더하기 빼기만
for i in range(N-a+1):
    for j in range(M-(b+c)+1):
        tmp = 0
        flag = False
        # 좌상단 좌표 -> arr[i][j]
        for n in range(a):
            for m in range(b+c):
                tmp += arr[i+n][j+m]
                if tmp > min_v:
                    flag = True
                    break
            if flag:
                break
        min_v = min(min_v, tmp)


# 2) 기역자
# 카라반이랑 차 값을 따로 구하고
# 옮기면서 더하기 빼기?
def common_shape(x, y, z):  # z에
    global min_v

    for i in range(N-(x+y)+1):
        for j in range(M-(z+x)+1):
            tmp = 0
            flag = False
            # 좌상단 좌표 arr[i][j]
            for n in range(x):
                for m in range(z):
                    tmp += arr[i+n][j+m]
                    if tmp > min_v:
                        flag = True
                        break
                if flag:
                    break

            if flag:
                continue

            for n in range(y):
                for m in range(x):
                    tmp += arr[n+i+x][m+j+z]
                    if tmp > min_v:
                        flag = True
                        break
                if flag:
                    break

            if flag:
                continue

            min_v = min(min_v, tmp)


common_shape(a, b, c)
if c != b:
    common_shape(a, c, b)

print(min_v)