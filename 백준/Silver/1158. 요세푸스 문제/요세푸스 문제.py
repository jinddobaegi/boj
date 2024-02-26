# 요세푸스 문제
# 실버 4

import sys

N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]

# 없앨 사람 담기
answer = []
# 사람 인덱스
n = 0

for t in range(N):
    n += K - 1
    if n >= len(arr):
        # 반복문 돌고 돌아올 때를 생각해서 나머지로 값을 바꿔주기
        n = n % len(arr)
    # 팝해줘야함
    answer.append(str(arr.pop(n)))
# 출력 형식에 맞게 join써서 해주기 + 뜨ㅣ어쓰기도
print("<", ", ".join(answer)[:], ">", sep="")
