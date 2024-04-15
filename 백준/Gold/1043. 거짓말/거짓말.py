# 서로소 집합
# 서로 중복 포함된 원소가 없는 집합들 -> 교집합이 없다
# 집합에 속한 특정 멤버, 대표자를 통해 각 집합들을 구분한다
# make-set, find-set, union 함수가 있음
# 서로소 집합을 만들기 위해 union find 알고리즘을 사용함
# 연결 리스트와 트리로 표현 가능
# 연결 리스트: 대표 하나, 다음 요소 하나씩 가리키도록
# 트리: 하나의 집합을 하나의 트리로 사용, 자식 노드가 부모 노드를 가리키며 루트 노드가 대표자가 된다
    # 트리(배열)을 이용해 저장

# make set(0~9)
# parent = [i for i in range(10)]  # 값 = 부모


# find set: 대표자를 찾음
def find_set(x):
    if parent[x] == x:
        return x

    # return find_set(parent[x])

    # 경로 압축
    parent[x] = find_set(parent[x])  # x의 부모를 재귀로 끝까지 찾아서 저장
    return parent[x]

# union: 같은 집합으로 만듦
def union(x, y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)

    if x == y:
        # print('사이클 발생')
        return

    # 2. 다른 집합이라면 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

#############################################################################

from sys import stdin

input = stdin.readline

# 과장된 이야기를 할 수 있는 파티 개수의 최댓값
# 파티에 진실을 아는 사람이 있으면? 그 파티는 제외

N, M = map(int, input().split())  # 사람 수 / 파티 수

parent = [i for i in range(N+1)]
true_info = list(map(int, input().split()))  # 진실 아는 사람 수
party_info = list(list(map(int, input().split())) for _ in range(M))

if true_info[0] == 0:
    print(M)

else:
    T = true_info[0]
    # true_info[1] 부터 true_info[M]까지는 트루맨의 번호임
    for t in range(1, T+1):
        union(0, true_info[t])

    # 파티를 한 번 싹 돌면서 진실을 아는 사람들의 집합을 만들고
    # 마지막에 다시 돌면서 진실을 아는 사람이 있는지 확인
    for i in range(M):
        party = party_info[i]
        n_of_party = party[0]

        # 모든 파티 사람들을 다 묶음
        for n in range(1, n_of_party):
            union(party[n], party[n+1])

    # 다 묶고 나서 처음부터 돌면서
    # 그 파티에 진실을 아는 사람이 있는지 확인
    res = 0

    for i in range(M):
        # 각 파티를 돌면서
        party = party_info[i]
        n = party[0]
        for j in range(1, n+1):
            # 진실을 아는 사람이 있으면
            if find_set(party[j]) == 0:
                break
        # 그 파티를 다 돌아도 진실을 아는 사람이 없으면
        else:
            res += 1

    print(res)