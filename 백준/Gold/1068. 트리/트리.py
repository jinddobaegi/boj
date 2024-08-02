from sys import stdin

input = stdin.readline

N = int(input())
pr = list(map(int, input().split()))
ch = [[] for _ in range(N)]
d = int(input())

# d 제거한 자식 리스트 생성 및 루트노드 확인
root = -1
for c in range(N):
    p = pr[c]
    if c != d:
        if p != d and p != -1:
            ch[p].append(c)

    if p == -1:
        root = c

# d를 지웠을 때
# 리프 노드의 개수

# 리프노드임을 아는 법?
# 자식이 없으면 리프노드임
# 루트 노트가 꼭 0이 아닐 수 있음

def dfs(v):
    global cnt

    if ch[v]:  # 자식 있는 경우
        for w in ch[v]:
            dfs(w)

    else:  # 자식 없는 경우
        cnt += 1
        return


cnt = 0
if root != d:
    dfs(root)
print(cnt)