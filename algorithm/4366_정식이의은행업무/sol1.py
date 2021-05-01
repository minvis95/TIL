import sys
sys.stdin = open("input.txt")

T = int(input())

def one_bit_revise(B):
    for i in range(len(B)):
        temp_B = B[:]
        number = 0
        if temp_B[i] == 0:
            temp_B[i] = 1
        else:
            temp_B[i] = 0
        for j in range(len(B)):
            number += temp_B[len(B) - j - 1] * (2**j)
        if num_base3(number):
            return number

def num_base3(number):
    revised_number = [0 for _ in range(len(T))]
    for i in range(len(T)-1, -1, -1):
        revised_number[i] = number % 3
        number //= 3
    return IsTrue(revised_number)

def IsTrue(revised_number):
    count = 0
    for i in range(len(T)):
        if revised_number[i] != T[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

for tc in range(1, T+1):
    B = [int(i) for i in input()]
    T = [int(i) for i in input()]
    result = one_bit_revise(B)
    print('#{} {}'.format(tc, result))

