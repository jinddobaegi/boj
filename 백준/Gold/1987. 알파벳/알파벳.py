R, C = map(int, input().split())
board = [input() for _ in range(R)]
max_v = 0

# 말 옮기는 로직
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
search = {(0, 0, board[0][0])}

while search and max_v < 26:
    i, j, word = search.pop()
    max_v = max(len(word), max_v)
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < R and 0 <= nj < C and board[ni][nj] not in word:
            search.add((ni, nj, word + board[ni][nj]))

print(max_v)