from sys import stdin

input = stdin.readline
N = int(input())
seq = list(map(int, input().split()))  # 중복 x
x = int(input())

seq.sort()

p1 = 0
p2 = N-1
cnt = 0
while p1 < p2:
    tmp = seq[p1] + seq[p2]
    if tmp == x:
        cnt += 1
        p1 += 1
        p2 -= 1
    elif tmp < x:
        p1 += 1
    else:
        p2 -= 1

print(cnt)