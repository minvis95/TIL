import sys
sys.stdin = open("input.txt")

T = int(input())

def check_babygin(numbers):
    counter = [0 for _ in range(10)]

    is_babygin = 0
    for number in numbers:
        counter[number] += 1

    # for idx in range(len(counter)):
    idx = 0
    while idx < len(counter):
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
            continue

        if idx < len(counter)-2:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                is_babygin += 1
                continue

        if is_babygin == 2:
            return 1
        idx += 1
    if is_babygin != 2:
        return 0

for tc in range(1, T+1):
    numbers = list(map(int, input()))
    result = check_babygin(numbers)


    print("#{} {}".format(tc, result))
