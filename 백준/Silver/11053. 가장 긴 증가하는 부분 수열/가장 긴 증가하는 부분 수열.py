n = int(input()) # 길이
arr = list(map(int, input().split())) # 배열
LIS = [arr[0]] # 일단 길이 1로 초기화! 여기에 가장 긴 수열 저장하기!

for i in arr:
    if LIS[-1] < i: # 가장 끝이 제일 큰 숫자니까 i 보다 작으면 넣어줭
        LIS.append(i)
    else:
        start = 0
        end = len(LIS) - 1
        while start <= end: # start가 end를 넘어서는 시점이 내가 가고자 하는 위치를 찾게 되는 것
            mid = (start + end) // 2

            if LIS[mid] < i:
                start = mid + 1
            else:
                end = mid - 1

        LIS[start] = i # 숫자가 직전 숫자보다 안크면 걍 바꿔끼워줭

print(len(LIS))