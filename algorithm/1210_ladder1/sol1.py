import sys
sys.stdin = open("input.txt")

T = 10

def ladder(ladder_matrix):
    dr = [1, 0, 0]
    dc = [0, -1, 1]
    for x in range(1, 101):
        if ladder_matrix[1][x] == 1:
            pivot_x = 1
            pivot_y = x
            trans = 0

            while pivot_x != 100:
                if trans == 0:
                    if ladder_matrix[pivot_x + dr[1]][pivot_y + dc[1]] == 1:
                        trans = 1
                        pivot_x += dr[trans]
                        pivot_y += dc[trans]
                        continue
                    if ladder_matrix[pivot_x + dr[2]][pivot_y + dc[2]] == 1:
                        trans = 2
                        pivot_x += dr[trans]
                        pivot_y += dc[trans]
                        continue
                    pivot_x += dr[trans]
                    pivot_y += dc[trans]

                elif trans == 1 or trans == 2:
                    # print(pivot_x, pivot_y)
                    if ladder_matrix[pivot_x + dr[0]][pivot_y + dc[0]] == 1:
                        trans = 0
                        pivot_x += dr[trans]
                        pivot_y += dc[trans]
                        continue
                    pivot_x += dr[trans]
                    pivot_y += dc[trans]

            if ladder_matrix[pivot_x][pivot_y] == 2:
                return x-1

for tc in range(1, T+1):
    no_need = input()
    ladder_matrix = []
    ladder_matrix.append([0] * 102)
    for _ in range(100):
        ladder_matrix += [[0] + list(map(int, input().split())) + [0]]
    ladder_matrix.append([0] * 102)
    result = ladder(ladder_matrix)
    print("#{} {}".format(tc, result))

