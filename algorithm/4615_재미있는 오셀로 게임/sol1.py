import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def count_place(N, M):
    # 상부터 시작하여 시계방향으로
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    # 보드판 만들기
    board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    middle = N // 2
    board[middle][middle] = 2
    board[middle + 1][middle + 1] = 2
    board[middle][middle + 1] = 1
    board[middle + 1][middle] = 1

    # 돌 놓기
    for place in places:
        board[place[0]][place[1]] = place[2]

        # 바뀔 수 있는 것 검사
        change_list = []
        for direction in range(8):
            x = place[0] + dx[direction]
            y = place[1] + dy[direction]
            while 1 <= x < N + 1 and 1 <= y < N + 1:
                # 돌이다르면 일단 어팬드, 0이나 오면 브레이크
                if board[x][y] != place[2] and board[x][y] != 0:
                    change_list.append([x, y])
                # break 되는 시점은 숫자 0 일때 밖에 없다.
                else:
                    break
                x += dx[direction]
                y += dy[direction]
            # 마지막 끝이 나와 같은 색이면 바꿔줄거야
            if 1 <= x < N + 1 and 1 <= y < N + 1 and board[x][y] == place[2]:
                # 색 바꿔줘(자기가 놓은 색으로)
                for change in change_list:
                    board[change[0]][change[1]] = place[2]
            # 아니였으면 다 없애
            else:
                change_list = []
    # count 세기
    count1 = 0
    count2 = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 검정
            if board[i][j] == 1:
                count1 += 1
            # 흰색
            elif board[i][j] == 2:
                count2 += 1
    return count1, count2

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    places = []
    for _ in range(M):
        places.append(list(map(int, input().split())))

    result1, result2 = count_place(N, M)
    print('#{} {} {}'.format(test_case, result1, result2))
