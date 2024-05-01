from sys import stdin

input = stdin.readline

# 연결하는 비용을 최소로 해라!
# 그때의 최소비용 출력!
# MST 문제

N = int(input())
M = int(input())

# Prim과 Kruskal 중 Kruskal을 써보자
# Prim은 시작점을 선택하면 거기서부터 가중치가 낮은
# 간선들을 그리디하게 찾아서 연결하는 반면
# Kruskal은 전체 중에서 가중치가 가장 낮은 선부터 선택하며
# 모든 정점이 연결될 때까지 진행
# 이때 간선을 선택하며 Union-Find를 사용해서
# 사이클 발생 여부, 즉 이미 연결된 노드들인지 확인!

# 간선 정보
edge = []

for _ in range(M):
    f, t, w = map(int, input().split())
    if f != t:
        edge.append([f, t, w])

edge.sort(key=lambda x: x[2])

# Make set
parents = [x for x in range(N+1)]  # 0 사용 안함

# Find set
def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

# Union
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같다 == 같은 집합이다
    if x == y:
        return

    # 대표자가 다르다 == 다른 집합인 경우
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


# Kruskal
def kruskal():
    cnt = 0
    total = 0
    for f, t, w in edge:
        if find_set(f) != find_set(t):
            cnt += 1
            total += w
            union(f, t)
            if cnt == N:
                break

    return total


res = kruskal()
print(res)