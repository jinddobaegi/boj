N, K = map(int, input().split())  # N: 사람 수, K: 제거 순서
people = list([p for p in range(N)])  # 사람
visited = list([0] * N)
res = '<'
turn = -1

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