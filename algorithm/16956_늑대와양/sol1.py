T = 1
def solution(R, C, check):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(R):
        for j in range(C):
            if garden[i][j] == 'W':
                for direct in range(4):
                    x = i + dr[direct]
                    y = j + dc[direct]
                    if 0 <= x <= R - 1 and 0 <= y <= C - 1:
                        if garden[x][y] == 'S':
                            check = False
                    if not check:
                        break
            if not check:
                break
        if not check:
            break
    if not check:
        print(int(check))
    else:
        print(int(check))
        for i in range(R):
            for j in range(C):
                if garden[i][j] == '.':
                    garden[i][j] = 'D'
            print(''.join(garden[i]))

for tc in range(1, T+1):
    R, C = map(int, input().split())
    garden = [list(input()) for _ in range(R)]
    check = True
    solution(R, C, check)

