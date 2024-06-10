# 가르침
# 골드4

'''
최대한 많은 단어 읽게 하기
dfs로 탐색해야할듯
'''

import sys
input = sys.stdin.readline


n, k = map(int, input().split())
words = [set(input().strip()[4:-4]) for _ in range(n)] # set으로 input 받으면서 중복 제거해줘

def dfs(s, cnt):
    global ans
    # a, c, i, n, t -> 무조건 배워야 돼
    # 최소한 k개는 배워야되니까..
    if cnt == k - 5:
        tmp = 0  # 현재 읽을 수 있는 단어 개수 저장

        # 목록 하나씩 확인하면서 돌면서
        for word in words:
            # 배운 글자로 해당 단어를 읽을 수 있는지 확인
            is_contain = True

            for w in word:
                # 배우지 않은 글자 있으면
                if not check[ord(w) - ord('a')]:
                    is_contain = False
                    break   # 단어 확인 중단

            # 해당 단어를 읽을 수 있는 경우
            if is_contain:
                tmp += 1  # 개수 check

        ans = max(ans, tmp)
        return

    for i in range(s, 26):
        if not check[i]:
            check[i] = True
            dfs(i, cnt + 1)
            check[i] = False

check = [0] * 26
ans = 0

# 가르칠 글자수 5보다 적을 ㄷ떄
if k < 5:
    # 읽을 수 있는 단어 x
    print(0)
    exit(0)

# 가르칠 글자수 26일 때
elif k == 26:
    # 전부 읽기 쌉 가능
    print(n)
    exit(0)

# a, c, i, n, t 는 무조건 배워야 돼
for w in ('a', 'c', 'i', 'n', 't'):
    check[ord(w) - ord('a')] = True

dfs(0, 0)
print(ans)