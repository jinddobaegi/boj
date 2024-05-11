from sys import stdin

input = stdin.readline


N = int(input())
arr = list(list(map(str, input().strip())) for _ in range(N))
visited = list(([0] * N) for _ in range(N))
cnt_list = list()

di = [1,0,-1,0]
dj = [0,1,0,-1]


def dfs(i, j):
    global cnt

    cnt += 1
    visited[i][j] = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]=='1' and not visited[ni][nj]:
            dfs(ni, nj)


for r in range(N):
    for c in range(N):
        if arr[r][c]=='1' and not visited[r][c]:
            cnt = 0
            dfs(r, c)
            if cnt:
                cnt_list.append(cnt)

print(len(cnt_list))
cnt_list.sort()
for cnt in cnt_list:
    print(cnt)