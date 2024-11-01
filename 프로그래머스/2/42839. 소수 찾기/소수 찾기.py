from itertools import permutations

def solution(numbers):
    def check_prime(x):
        for c in range(2, x):
            if x%c == 0:
                return False
        return True
    
    answer = 0
    used = set()
    for r in range(1, len(numbers)+1):
        perms = permutations(tuple(numbers), r)
        for perm in perms:
            num = ''
            for p in perm:
                num += p
            num = int(num)
            if num > 1 and num not in used:
                used.add(num)
                if check_prime(num):
                    answer += 1
    
    return answer