import sys
sys.stdin = open("input.txt")

T = int(input())

def check_gravity(numbers):
    # 최대 중력을 0으로 세팅
    max_gravity = 0
    # 모든 원소를 돌면서 자기자신의 최대중력을 구함
    for i in range(len(numbers)):
        # 상자가 없으면 할 필요없이 continue
        if numbers[i] == 0:
            continue

        # 자기 자신의 최대중력 0으로 세팅
        my_gravity = 0
        # 자기 위치에서 최대로 나올 수 있는 중력값
        my_gravity = len(numbers) - i - 1

        # 자기 오른쪽에 있는 column의 상자수와 비교해야함
        for j in range(i+1, len(numbers)):
            # 자기보다 많이 쌓인 상자가 있네?
            if numbers[i] <= numbers[j]:
                # then 나의 중력값은 1이 감소
                my_gravity -= 1
        # 현재의 최대중력과 비교해!
        if my_gravity > max_gravity:
            # then 갱신
            max_gravity = my_gravity
    return max_gravity


for tc in range(1, T+1):
    # numberT의 개수를 입력받음.(입력만 받고 사용x)
    length = input()
    # list로 입력 받아옴
    numbers = list(map(int, input().split()))
    # 자기자신이 가지는 최대 중력을 구하고 최대 중력 갱신하고 return하는 함수
    result = check_gravity(numbers)
    print("#{} {}".format(tc, result))

