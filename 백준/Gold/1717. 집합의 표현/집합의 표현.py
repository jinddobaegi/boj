from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

# 1) 0~n까지 있더라 == make-set
# 2) 합집합 연산 == union
# 3) 같은 집합에 속하는지 확인 == find-set

def find_set(x):
    if par[x] == x:
        return x  # 밑에 있는 재귀 빠져나올 때까지만 사용됨

    par[x] = find_set(par[x])  # 여기서 마지막 if문의 return 사용되고
    return par[x]  # 최종 return이 있어야 None값 안 나옴


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        par[y] = x
    else:
        par[x] = y


N, M = map(int, input().split())
par = [x for x in range(N+1)]  # make-set
for _ in range(M):
    flag, a, b = map(int, input().split())
    if flag == 1:  # find-set
        if find_set(a) == find_set(b):
            print("yes")
        else:
            print("no")
    else:  # union
        union(a, b)