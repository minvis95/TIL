import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    triangle_list = [[0 for _ in range(N+1)] for _ in range(N+1)]
    triangle_list[1][1] = 1
    print("#{}".format(tc))
    print(triangle_list[1][1])
    for i in range(2, N + 1):
        for j in range(1, i):
            triangle_list[i][j] = triangle_list[i-1][j] + triangle_list[i-1][j-1]
            print(triangle_list[i][j], end=' ')
        triangle_list[i][i] = 1
        print(triangle_list[i][i], end='')
        print()