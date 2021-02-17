import sys
sys.stdin = open("input.txt")

T = int(input())

def binary_search(P, x):
    start = 1
    end = P
    cnt = 0
    middle = 0
    while start <= end:
        middle = (start + end) // 2
        cnt += 1
        if x == middle:
            return cnt
        elif x > middle:
            start = middle
        else:
            end = middle
    return False

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    count_A, count_B = 0, 0
    count_A = binary_search(P, A)
    count_B = binary_search(P, B)
    if count_A > count_B:
        result = 'B'
    elif count_A < count_B:
        result = 'A'
    else:
        result = 0

    if count_A == False and count_B > 0:
        result = 'B'
    elif count_B == False and count_A > 0:
        result = 'A'
    elif count_A == False and count_B == False:
        result = 0

    print("#{} {}".format(tc, result))

