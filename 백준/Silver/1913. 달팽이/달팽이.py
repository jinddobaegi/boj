from sys import stdin

input = stdin.readline

N = int(input())
target = int(input())

# 일단 배열을 만들어서 출력
# 그 후 T의 좌표를 출력

arr = list([0] * N for _ in range(N))

# 시작점
# 홀: 행, 열 둘 다 (n+1)//2
# 짝: 행: n//2+1, 열: n//2

# 끝점
# 홀: 1,1
# 짝: n,n

# 코드에선 idx 고려해서 -1씩 하자
r = c = 0  # 시작점 init
if N % 2:  # 홀
    r = c = (N+1)//2 - 1
else:  # 짝
    r = N//2
    c = (N//2) - 1

arr[r][c] = 1
target_r, target_c = r+1, c+1  # target 만나면 저장
r -= 1  # 2를 넣을 위치로 미리 조정

t = 1  # 2~N까지 시점을 나타낼 것임
num = 1  # 넣을 숫자
while t != N:
    t += 1
    num_of_new = t*2 - 1  # N이 1씩 커질 때마다 새로 생기는 칸 수
    corner = num_of_new//2  # 꺾을 순간 확인용
    for i in range(num_of_new):
        num += 1
        if num == target:
            target_r = r+1
            target_c = c+1
        arr[r][c] = num
        if t % 2:  # t가 홀수
            if i < corner:
                c -= 1
            else:
                r -= 1
        else:  # t가 짝수
            if i < corner:
                c += 1
            else:
                r += 1


for nums in arr:
    print(*nums)

print(target_r, target_c)
