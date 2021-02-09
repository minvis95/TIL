import sys
sys.stdin = open("input.txt")

T = int(input())


def subtraction(N, M, numbers):
    # M개 끼리 더한 것을 저장하기 위해 필요한 공간은 N-M+1개 이다.
    sum_list = [0]*(N-M+1)

    # sum_list의 idx에 접근하기 위해 range사용
    for i in range(len(sum_list)):
        # 구간합을 구하기 위해 M을 사용해서 idx 접근
        # 인덱스 오류 안남 range(len(sum_list))으로 했기때문에
        for j in range(M):
            sum_list[i] += numbers[i + j]

    # 최대 최소 구하기
    min_number, max_number = sum_list[0], sum_list[0]
    for sum in sum_list:
        if min_number > sum:
            min_number = sum
        if max_number < sum:
            max_number = sum

    return max_number - min_number

for tc in range(1, T+1):
    # 숫자가 N개있어요, M개 끼리 더하세요~
    N_M = list(map(int, input().split()))
    N = N_M[0]
    M = N_M[1]
    # N개의 숫자 가져오기
    numbers = list(map(int, input().split()))

    result = subtraction(N, M, numbers)

    print("#{} {}".format(tc, result))

