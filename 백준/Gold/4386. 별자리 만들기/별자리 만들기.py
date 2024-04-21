from sys import stdin

input = stdin.readline

V = int(input())
E = V-1


# 좌표가 주어지면 거리 구하는 함수
def get_dist(x1, y1, x2, y2):
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    dist = round(dist, 2)
    return dist


# 별 좌표 저장
stars = []
for _ in range(V):
    x, y = map(float, input().split())
    stars.append((x, y))

# 모든 별 간 거리를 저장할 것임
edge = []
for i in range(V):
    for j in range(V):
        if i >= j:
            continue

        # i 별과 j 별의 거리가 d라고 한다면
        # (i, j, d) 이런 식으로 graph에 저장할 것임
        d = get_dist(*stars[i], *stars[j])
        edge.append((i, j, d))

edge.sort(key=lambda x: x[2])  # 거리로 정렬

# print(edge)  # 별 간 거리 확인


### Kruskal을 위한 Union-find 준비
# 1) make-set
parents = [i for i in range(V)]


# 2) find-set
def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


# 3) union-find
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


# Kruskal
def kruskal():
    cnt = 0
    total = 0
    # edge에서 짧은 애들 하나씩 뽑아서
    for f, t, w in edge:
        # 사이클 발생 안 하면
        if find_set(f) != find_set(t):
            # 유니온하고 거리 누적합
            union(f, t)
            total += w
            cnt += 1

            # 종료 조건은 cnt == V
            if cnt == V:
                break

    return total


res = kruskal()
print(res)