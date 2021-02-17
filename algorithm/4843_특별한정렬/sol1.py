import sys
sys.stdin = open("input.txt")

T = int(input())

def select_sort(N, A):
    for i in range(1, N//2 + 1):
        max_index = 2*(i-1)
        min_index = 2*(i-1) + 1
        for j in range(2*(i-1)+1, N):
            if A[max_index] < A[j]:
                max_index = j
        A[2 * (i - 1)], A[max_index] = A[max_index], A[2 * (i - 1)]
        for j in range(2 * (i-1) + 2, N):
            if A[min_index] > A[j]:
                min_index = j
        A[2 * (i - 1) + 1], A[min_index] = A[min_index], A[2 * (i - 1) + 1]
    return A

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    result = []
    result = select_sort(N, A)
    print("#{}".format(tc), end=' ')
    for i in range(0, 10):
        print("{}".format(result[i]), end=' ')
    print()

