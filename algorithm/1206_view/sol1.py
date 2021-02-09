import sys
sys.stdin = open("input.txt")

T = 10

def good_layer(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            continue

        for number in range(numbers[i],0,-1):
            if number > numbers[i-1] and number > numbers[i-2] and number > numbers[i+1] and number > numbers[i+2]:
                count += 1
            else:
                break
    return count

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = good_layer(numbers)

    print("#{} {}".format(tc, result))

