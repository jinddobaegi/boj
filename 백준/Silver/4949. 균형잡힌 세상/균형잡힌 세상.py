from collections import deque

# 스택 활용
# 문자열 무시
# . 나오면 종료
# 여는 괄호면 push, 닫는 괄호면 pop

my_dict = {
    ')': '(',
    ']': '['
}

while True:
    # 스택은 후입 선출 구조
    stack = deque()
    my_sentence = input()
    isBalanced = True
    if my_sentence == '.':
        break
    try:
        for x in my_sentence:
            if x == '.':
                break
            elif x in '([':
                stack.append(x)
            elif x in ')]':
                if not stack:
                    isBalanced = False
                    break
                else:
                    pop_char = stack.pop()
                    if pop_char != my_dict[x]:
                        isBalanced = False
                        break
        if not stack and isBalanced:
            print('yes')
        else:
            print('no')

    except EOFError:
        break
