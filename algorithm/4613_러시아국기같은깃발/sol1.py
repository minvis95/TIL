import sys
sys.stdin = open("input.txt")

T = int(input())

def painting(N, M):
    paint_white = 0
    min_count = N*M
    for white in range(0, N - 2):
        paint_white += M - matrix[white].count('W')

        paint_blue = 0
        for blue in range(white+1, N - 1):
            paint_blue += M - matrix[blue].count('B')

            paint_red = 0
            for red in range(blue+1, N):
                paint_red += M - matrix[red].count('R')

            all_paint = paint_white + paint_blue + paint_red
            if min_count > all_paint:
                min_count = all_paint
    return min_count
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(' '.join(input()).split()))

    result = painting(N, M)

    print("#{} {}".format(tc, result))

