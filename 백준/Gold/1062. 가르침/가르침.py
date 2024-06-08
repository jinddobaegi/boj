N, K = map(int, input().split())
words = list(input().lstrip("anta").rstrip("tica") for _ in range(N))
educated = [0] * 26  # 알파벳의 개수

# K개의 글자를 가르쳤을 때
# 학생들이 읽을 수 있는 단어 개수의 최댓값 출력

# K개의 글자가 뭔지는 알 수 없음
# 따라서 가장 많이 읽을 수 있게 하는 경우 중
# 가르치는 글자가 K개 이하인 것 중에 가장 큰 경우를 고르면 됨
# 일단 뭔가 브루트포스 돌려도 될 것 같음

# 1) K개의 글자를 선택
# 2) 선택이 다 되면 그때의 읽을 수 있는 단어 수 업데이트

# 있는 애들은 표시
a_ord = ord('a')
for c in 'antic':
    x = ord(c) - a_ord
    educated[x] = 1


# 조건에 맞을 때 사용할
# 단어 체크 함수
def word_check():
    cnt = 0
    for word in words:
        for char in word:
            char_ord = ord(char) - a_ord
            if not educated[char_ord]:
                break
        else:
            cnt += 1

    return cnt


def dfs(t, depth):  # 이 함수는 K >= 5일 때만 사용할 것임
    global max_v

    if t == 26 or depth == K-5:
        # 조건에 맞으면 단어 체크
        max_v = max(max_v, word_check())
        return
    
    # t번째 글자 모르는 경우
    if not educated[t]:
        # t번째 글자를 가르치는 경우
        educated[t] = 1
        dfs(t+1, depth+1)

        # t번째 글자를 몰라도 안 가르치고 넘어가는 경우
        educated[t] = 0
        dfs(t+1, depth)

    # t번째 글자 아는 경우
    else:
        dfs(t+1, depth)
        
    # for i in range(t, 26):
    #     if not educated[i]:
    #         # i번째 글자를 가르치는 경우
    #         educated[i] = 1
    #         dfs(i, depth+1)
    #         # i번째 글자를 가르치치 않고 넘어가는 경우
    #         educated[i] = 0


max_v = 0
if K == 26:
    max_v = N
elif K >= 5:
    dfs(0, 0)

print(max_v)