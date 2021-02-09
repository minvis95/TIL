import sys
sys.stdin = open("input.txt")

T = 10

def flattening(dump_count, numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers += number

    while dump_count > 0:
        maximum, minimum = numbers[0], numbers[0]
        max_idx, min_idx = 0, 0
        for idx in range(len(numbers)):
            if maximum < numbers[idx]:
                maximum = numbers[idx]
                max_idx = idx
            if minimum > numbers[idx]:
                minimum = numbers[idx]
                min_idx = idx

        if maximum == minimum:
            return 0
        if maximum == minimum + 1 and sum_numbers % 2:
            return 1

        numbers[max_idx] -= 1
        numbers[min_idx] += 1
        dump_count -= 1
    # 이것을 함수로 하면 코드 길이는 줄어들긴 하겠네.
    maximum, minimum = numbers[0], numbers[0]
    max_idx, min_idx = 0, 0
    for idx in range(len(numbers)):
        if maximum < numbers[idx]:
            max_idx = idx
            maximum = numbers[idx]
        if minimum > numbers[idx]:
            min_idx = idx
            minimum = numbers[idx]
    return numbers[max_idx] - numbers[min_idx]


for tc in range(1, T+1):
    dump_count = int(input())
    numbers = list(map(int, input().split()))
    result = flattening(dump_count, numbers)

    print("#{} {}".format(tc, result))

