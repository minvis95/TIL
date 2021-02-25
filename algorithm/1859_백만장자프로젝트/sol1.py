import sys
sys.stdin = open("input.txt")

T = int(input())
def good_seller(start, end):
    if start >= end:
        return 0
    # 최댓값을 가지는 index 찾아
    max_index = start
    for i in range(start, end + 1):
        if numbers[max_index] < numbers[i]:
            max_index = i

    return (numbers[max_index] * len(numbers[start:max_index])) - sum(numbers[start:max_index]) + good_seller(max_index + 1, end)

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = good_seller(0, N - 1)
    print("#{} {}".format(tc, result))

