import sys
sys.stdin = open("input.txt")

T = int(input())

def max_prize(numbers, count, i_idx):
    # base case
    if count == 0:
        return int(''.join(numbers))

    # 완전 탐색
    result = []

    for i in range(i_idx, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] <= numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                result.append(max_prize(numbers, count-1, i))
                numbers[j], numbers[i] = numbers[i], numbers[j]

    max_result = 0
    for number in result:
        if max_result < number:
            max_result = number
    return max_result

def bubble_sort_reverse(numbers):
    numbers = list(map(int, numbers))

    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    numbers.reverse()
    return numbers

for tc in range(1, T+1):

    numbers, count = input().split()
    numbers = list(numbers)
    count = int(count)

    copy_result = 0
    # 내림차순인 numbers이면 max_prize를 수행할 수 없으므로 따로 처리해줘야한다.
    if bubble_sort_reverse(numbers) == list(map(int, numbers)):
        copy_count = count
        copy_numbers = numbers[:]
        while copy_count > 0:
            copy_numbers[-1], copy_numbers[-2] = copy_numbers[-2], copy_numbers[-1]
            copy_count -= 1
        copy_result = int(''.join(copy_numbers))

    result = 0
    result = max_prize(numbers, count, 0)

    if copy_result > result:
        print("#{} {}".format(tc, copy_result))
    else:
        print("#{} {}".format(tc, result))

