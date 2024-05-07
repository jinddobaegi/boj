from sys import stdin

input = stdin.readline

N = int(input())

arr = list(map(int, input().split()))

# set에 넣고 길이 재는 걸로는 "틀렸습니다"가 뜬단 말이지...

'''
부분수열?
주어진 수열의 일부 항을 원래 순서대로 나열하여 얻을 수 있는 수열
즉 순서를 바꾸면 안됨


나무위키, "최장 증가 부분 수열" 참고함

부분 수열의 "길이를 측정하기 위해서"
0이 들어있는 배열을 하나 만든다 (sub_seq, 이하 ss)
arr를 돌면서 해당 원소(이하 x)가 ss의 마지막 원소보다 크면 그냥 넣고, 같으면 지나친다
만약 x가 ss의 마지막 원소보다 작은 경우는
ss에서 x가 비집고 들어갈 수 있는 위치를 찾는다

그래서 ss에서
x보다 큰 수 중, 최저를 찾으면
그 위치에 x를 넣는다

왜냐하면 arr에서 부분수열 개수를 셀 때,
여러 가지 경우의 수가 있을 텐데
새로 등장한 x부터 다시 셀 수도 있고,
이전에 저장된 순서로 셀 수도 있기 때문이다.

그래서 최저값을 삽입하는 과정을 반복하다보면
나중에, 결론적으로는 답이 안되는 더 작은 수(a)가 들어온다고 해도,
새로 등장한 x가 ss의 마지막 원소보다 크다면
a 때문에 ss의 정보는 바뀌어 있지만,
길이를 측정하는 측면에서는 a에 상관없이 그 길이가 유지되고 있는 것이다.

a는 그냥 가능성때문에 저장되어있는 것이다.
'''


def bin_search(len_of_ss, target):
    start = 0
    end = len_of_ss-1
    while start <= end:
        mid = (start+end)//2
        if sub_seq[mid] == target:
            return mid

        elif sub_seq[mid] > target:
            end = mid-1

        else:
            start = mid+1

    return start


sub_seq = [0]

for x in arr:
    if sub_seq[-1] < x:
        sub_seq.append(x)

    else:
        # ss에서 x보다 큰 값 중 가장 작은 값을 찾아야 함
        # 그 위치에 x를 삽입
        tmp_idx = bin_search(len(sub_seq), x)
        sub_seq[tmp_idx] = x

print(len(sub_seq)-1)