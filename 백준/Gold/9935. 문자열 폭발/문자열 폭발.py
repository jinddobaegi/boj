inlst = input()
bomb = input()
len_bomb = len(bomb)
ans = []

for i in inlst:
    ans.append(i)
    if bomb[-1] == ans[-1] and ''.join(ans[-len_bomb:]) == bomb:
        del ans[-len_bomb:]

print(''.join(ans) if ans else 'FRULA')