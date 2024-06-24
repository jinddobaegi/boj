from sys import stdin

input = stdin.readline

A = input().rstrip()
B = input().rstrip()

len_a = len(A)
len_b = len(B)

LCS = [[''] * (len_b+1) for _ in range(len_a+1)]

for i in range(1, len_a+1):
    for j in range(1, len_b+1):
        if A[i-1] == B[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + B[j-1]
        else:
            if len(LCS[i][j-1]) > len(LCS[i-1][j]):
                LCS[i][j] = LCS[i][j-1]
            else:
                LCS[i][j] = LCS[i-1][j]

lcs = LCS[-1][-1]
len_lcs = len(lcs)
if len_lcs > 0:
    print(len_lcs)
    print(lcs)
else:
    print(0)