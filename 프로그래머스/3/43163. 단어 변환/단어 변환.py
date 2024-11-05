from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    
    arr = tuple(chr(i) for i in range(97, 123))
    
    n = len(begin)
    q = deque([(0, begin)])
    used_words = {begin,}
    while q:
        cnt, word_now = q.popleft()
        cnt += 1
        for i in range(n):  # 각 자리수 바꿔보기
            for a in arr:
                word_next = word_now[:i] + a + word_now[i+1:]
                if word_next == target:
                    return cnt
                if word_next in words and word_next not in used_words:
                    q.append((cnt, word_next))
                    used_words.add(word_next)
    
    return answer