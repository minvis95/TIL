import sys
sys.stdin = open("input.txt")

T = int(input())

def snail_matrix(N):
    result = [[0 for _ in range(N)] for _ in range(N)]
    row = 0
    col = -1
    count = 1
    pivot = 1
    while N > 0:
        for _ in range(N):
            col += pivot
            result[row][col] = count
            count += 1
        N -= 1
        for _ in range(N):
            row += pivot
            result[row][col] = count
            count += 1
        pivot *= -1
    return result

for tc in range(1, T+1):
    N = int(input())
    result = []
    result = snail_matrix(N)
    print("#{}".format(tc))
    for i in range(len(result)):
        print(*result[i])