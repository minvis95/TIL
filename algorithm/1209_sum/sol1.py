import sys
sys.stdin = open("input.txt")

T = 10

def max_sum(input_list):
    sum_list = []
    for i in range(len(input_list)):
        sum_value = 0
        for j in range(len(input_list[0])):
            sum_value += input_list[i][j]
        sum_list.append(sum_value)

    for i in range(len(input_list[0])):
        sum_value = 0
        for j in range(len(input_list)):
            sum_value += input_list[j][i]
        sum_list.append(sum_value)

    # LtoR
    sum_value = 0
    for i in range(len(input_list)):
        sum_value += input_list[i][i]
    sum_list.append(sum_value)

    # RtoL
    sum_value = 0
    for i in range(len(input_list)):
        sum_value += input_list[i][len(input_list)-i-1]
    sum_list.append(sum_value)

    max_value = 0
    for value in sum_list:
        if max_value < value:
            max_value = value
    return max_value

for tc in range(1, T+1):
    input_list = []
    test_case = int(input())
    for i in range(100):
        input_list += [list(map(int, input().split()))]

    result = 0
    result = max_sum(input_list)

    print("#{} {}".format(tc, result))

