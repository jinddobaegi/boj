# 1 떼고, 2 떼고... 하면서 뗄 수 없을 때까지..?

S = int(input())
cnt = 0
num = 1
while True:
    S -= num
    if S >= 0:
        num += 1
        cnt += 1
    else:
        break

print(cnt)