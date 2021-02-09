import sys
sys.stdin = open("input.txt")

T = int(input())

def maximum(numbers):
    max_number = 0
    for number in numbers:
        if max_number < number:
            max_number = number
    return max_number
def minimum(numbers):
    min_number = 0
    for number in numbers:
        if min_number == 0:
            min_number = number

        if min_number > number:
            min_number = number
    return min_number

for tc in range(1, T+1):
    N = input()
    numbers = list(map(int, input().split()))
    result = 0
    result = maximum(numbers) - minimum(numbers)
    print("#{} {}".format(tc, result))

