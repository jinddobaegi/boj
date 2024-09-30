from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)

N = int(input())

# 장대는 무조건 세 개
# 항상 위가 아래보다 작아야 함


# 참조자료: https://youtu.be/FYCGV6F1NuY
def solution(num, start, goal, sub):  # 안 옮긴 원반 개수, 옮기기 전 기둥, 옮긴 뒤 기둥, 나머지 기둥
    # 1) start 원반이 한 개 남으면 print
    if num == 1:
        print(start, goal)
        return

    # 2) 가장 큰 원반 제외하고 N-1개의 원반을 "현재 기둥"에서 모두 "보조 기둥"으로 옮기기
    solution(num-1, start, sub, goal)
    # 3) 시작 기둥에 남은 가장 큰 원반 "현재 기둥" -> "목표 기둥"
    print(start, goal)
    # 4) "보조 기둥"에 옮겨놓은 n-1개의 원반들 "목표 기둥"으로 옮기기
    solution(num-1, sub, goal, start)


print(2**N-1)
solution(N, 1, 3, 2)