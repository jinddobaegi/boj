def solution(brown, yellow):
    answer = []  # 가로, 세로 길이 담자
    # 가/세 최소 3 이상
    # 가로 x, 세로 y 라면
    # 노란사각형은 가로 x-2, 세로 y-2
    # 총 칸 수를 통해 가능한 가/세 경우의 수 중 완탐
    total = brown + yellow
    y = 3
    while y <= total//2:
        if total % y:
            y += 1
            continue
            
        x = total // y
        if (x-2)*(y-2) == yellow:
            answer = [x, y]
            break
        else:
            y += 1
    
    return answer