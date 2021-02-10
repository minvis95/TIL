import sys
sys.stdin = open("input.txt")

T = int(input())


def max_multiplication(A_list, B_list):


    if len(A_list) >= len(B_list):
        max_list = A_list[:]
        min_list = B_list[:]
    else:
        max_list = B_list[:]
        min_list = A_list[:]

    maximum = 0
    for i in range(len(max_list)-len(min_list)+1):
        mul_and_add = 0
        for j in range(0, len(min_list)):
            mul_and_add += max_list[j+i] * min_list[j]
        if maximum < mul_and_add:
            maximum = mul_and_add
    return maximum

for tc in range(1, T+1):
    N_M = list(map(int, input().split()))
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    result = 0
    result = max_multiplication(A_list, B_list)

    print("#{} {}".format(tc, result))

