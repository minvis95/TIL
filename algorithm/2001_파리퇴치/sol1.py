import sys
sys.stdin = open("input.txt")

T = int(input())

def kill_insect(matrix, N, M):
    result = []
    for row in range(N-M+1):
        for col in range(N-M+1):
            sum_subset = 0
            for i in range(M):
                for j in range(M):
                    sum_subset += matrix[i+row][j+col]
            result.append(sum_subset)

    max_value = 0
    for number in result:
        if max_value < number:
            max_value = number

    return max_value

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix += [list(map(int, input().split()))]
    result = kill_insect(matrix, N, M)
    print("#{} {}".format(tc, result))

