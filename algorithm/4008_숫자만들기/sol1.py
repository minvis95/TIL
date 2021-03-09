import sys
sys.stdin = open("input.txt")

T = int(input())

def cal(untill_count, N, count, add, sub, mul, div):
    global min_value, max_value
    # base_case
    if N == count:
        if max_value < untill_count:
            max_value = untill_count

        if min_value > untill_count:
            min_value = untill_count

    # 모든 경우의 수 다 조사
    else:
        if add > 0:
            cal(untill_count + numbers[count], N, count + 1, add - 1, sub, mul, div)

        if sub > 0:
            cal(untill_count - numbers[count], N, count + 1, add, sub - 1, mul, div)

        if mul > 0:
            cal(untill_count * numbers[count], N, count + 1, add, sub, mul - 1, div)

        if div > 0:
            cal(int(untill_count / numbers[count]), N, count + 1, add, sub, mul, div - 1)


for tc in range(1, T+1):
    N = int(input())
    add, sub, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))
    min_value = 10000000000
    max_value = -10000000000
    cal(numbers[0], N, 1, add, sub, mul, div)
    print('#{} {}'.format(tc, max_value - min_value))

