# 전, 중, 후위 순회
# 이진 트리
# A가 무조건 루트 노드
# A부터 차례대로 매겨짐

# ord()를 써서 -64 해서
# 숫자로 바꾸자(1~26)
# 되돌릴 땐 +64 하고 chr()

pre_list = []
in_list = []
post_list = []


def preorder(i):
    if i:
        # VLR
        pre_list.append(chr(i + 64))
        preorder(ch_left[i])
        preorder(ch_right[i])


def inorder(i):
    if i:
        # LVR
        inorder(ch_left[i])
        in_list.append(chr(i + 64))
        inorder(ch_right[i])


def postorder(i):
    if i:
        # LRV
        postorder(ch_left[i])
        postorder(ch_right[i])
        post_list.append(chr(i + 64))


N = int(input())

ch_left = [0] * (N+1)
ch_right = [0] * (N+1)

# ord(알파벳) - 64
# A~Z -> 1~26
for _ in range(N):
    mid, left, right = map(str, input().split())
    mid = int(ord(mid) - 64)

    if left != '.':
        left = int(ord(left) - 64)
        ch_left[mid] = left

    if right != '.':
        right = int(ord(right) - 64)
        ch_right[mid] = right

preorder(1)
inorder(1)
postorder(1)

print(*pre_list, sep='')
print(*in_list, sep='')
print(*post_list, sep='')