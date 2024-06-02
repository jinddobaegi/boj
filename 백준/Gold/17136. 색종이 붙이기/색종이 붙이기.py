from sys import stdin

input = stdin.readline

'''
처음에는 큰 색종이부터 체크하는 방식으로 풀었음
17%쯤에서 막힘, 그래서 눈물을 머금고 코드를 갈아엎음
아래가 그 반례임

0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
'''

arr = list(list(map(int, input().split())) for _ in range(10))
paper_dict = {
    1: 5,
    2: 5,
    3: 5,
    4: 5,
    5: 5,
}
res = 26

# 크기 별 색종이를 다 대보는 방법을 사용


# 특정 칸에서 k*k만큼의 1이 있는지 확인하는 함수
def recon(y, x, k):
    for i in range(k):
        for j in range(k):
            if arr[y+i][x+j] == 0:
                return False

    return True


# 한 칸마다 함수를 재귀적으로 사용할 것임
def my_func(r, c, cnt):
    global res

    # 행 꽉차면 결과 return
    if r >= 10:
        res = min(res, cnt)
        return

    # 열 꽉차면 다음 행으로
    if c >= 10:
        my_func(r+1, 0, cnt)
        return

    # 특정 칸에서 종이를 사이즈 별로 다 대볼 건데
    # 해당 칸에서 k*k를 놓을 수 있는지 보고
    # 놓을 수 있으면
    # 놓는 다고 가정하고 재귀 후
    # 다시 안 놓은 것처럼 하고 다음 크기의 종이를 대볼 것임
    if arr[r][c]:
        for k in range(1, 6):
            if paper_dict[k] == 0:  # k*k가 없는 경우
                continue

            if r+k-1 >= 10 or c+k-1 >= 10:  # 범위를 넘어가는 경우
                continue

            if not recon(r, c, k):
                break

            # 가능한 경우 -> k*k 놓는 경우
            for i in range(k):
                for j in range(k):
                    arr[r+i][c+j] = 0

            paper_dict[k] -= 1

            my_func(r, c+k, cnt+1)  # 어차피 k만큼 1을 지워서 바로 k칸만큼 이동

            # k*k 안 놓는 경우
            paper_dict[k] += 1
            for i in range(k):
                for j in range(k):
                    arr[r+i][c+j] = 1

    else:
        my_func(r, c+1, cnt)


my_func(0, 0, 0)
print(-1 if res == 26 else res)