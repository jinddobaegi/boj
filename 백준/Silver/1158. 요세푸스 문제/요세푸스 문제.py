# 요세푸스 문제
# N과 K가 주어짐
# 1 ~ N번 사람이 원 그리고 앉음
# K번째 사람 제거
# 그 다음 K번째 사람 제거
# N명이 모두 제거될 때까지 반복
# 이때 제거되는 순서를 요세푸스 순열이라고 함

N, K = map(int, input().split())  # N: 사람 수, K: 제거 순서
people = list([p for p in range(N)])  # 사람
visited = list([0] * N)
res = '<'
turn = -1

# 시간 초과
# for i in range(N):
#     for k in range(1, K+1):
#         turn = (turn + 1) % N
#         while visited[turn] == 1:
#             turn = (turn + 1) % N
# 
#     res += f'{people[turn] + 1}, '
#     visited[turn] = 1
# 
# res = res[:-2]
# res += '>'
# print(res)

while people:
    turn = (turn + K) % len(people)
    x = people[turn]
    # print(x)
    people.remove(x)
    # print(people)
    res += f'{x + 1}, '
    turn -= 1

res = res[:-2]
res += '>'
print(res)
