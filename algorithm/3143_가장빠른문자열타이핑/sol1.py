import sys
sys.stdin = open("input.txt")

T = int(input())

def min_count(A, B):
    count = 0
    while True:
        if B in A:
            A = A.replace(B, '', 1)
            count += 1
        else:
            return len(A) + count
for tc in range(1, T+1):
    A, B = input().split()

    result = min_count(A, B)
    print("#{} {}".format(tc, result))

