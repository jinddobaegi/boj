# N-Queen
# 각 행과 열에는 하나의 퀸만 존재할 수 있다

N = int(input())

def attack(a):
    for i in range(a):
        # 같은 열에 있거나 대각선에 있다면?
        if arr[a] == arr[i] or abs(arr[a] - arr[i]) == abs(a - i):
            return False
    return True

def n_queens(start):
    global ans
    if start == N:
        ans += 1
    else:
        for i in range(N):
            arr[start] = i # (start, i)
            if attack(start): # 퀸을 놓을 수 있으면?
                n_queens(start + 1)

arr = [0] * N
ans = 0
n_queens(0)
print(ans)