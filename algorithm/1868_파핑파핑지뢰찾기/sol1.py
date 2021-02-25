import sys
sys.stdin = open("input.txt")

T = int(input())

def click_count(N):
    # 상부터 시작하여 시계방향으로
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    count = 0
    # 연쇄반응 터지는거랑 주변에 지뢰 없는 것만!! 조사 들어감
    for i in range(N):
        for j in range(N):
            # '.' 만 조사
            if matrix[i][j] != '.':
                continue
            # 겉테두리 조사
            border = []
            for direction in range(8):
                x = i + dx[direction]
                y = j + dy[direction]
                if 0 <= x < N and 0 <= y < N:
                    # matrix[i][j]는 연쇄반응을 일으키는 주범이 아니다.
                    if matrix[x][y] == '*':
                        break
                    border.append([x, y])
            # 사방팔방에 지뢰 없으면
            else:
                count += 1
                matrix[i][j] = 0
                calculate_count(border)

    # 연쇄반응하는 것들 다 끝났으면 '.'에 개수만 세면 끝
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '.':
                count += 1
    return count

def calculate_count(border):
    # 상부터 시작하여 시계방향으로
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    while len(border):
        count = 0
        arround_border = []
        x, y = border[0]
        border.pop(0)
        # 숫자로 표현된 좌표면 조사한 것이므로 할 필요가 없다.
        if matrix[x][y] != '.':
            continue

        # 사방팔방 둘러봐
        for direction in range(8):
            around_x = x + dx[direction]
            around_y = y + dy[direction]
            # 일단 범위에 있어야해
            if 0 <= around_x < N and 0 <= around_y < N:
                # 지뢰있네? 추가
                if matrix[around_x][around_y] == '*':
                    count += 1
                # .이네?? 일단 추가시켜 연쇄반응 터질지도 모르니깐
                elif matrix[around_x][around_y] == '.':
                    arround_border.append([around_x, around_y])
        # 내 사방팔방에는 지뢰가 없어
        if count == 0:
            matrix[x][y] = count
            # 내 주변 지뢰들의 count도 보고싶어
            border += arround_border
        # 지뢰가 있네.. 그냥 숫자만..
        else:
            matrix[x][y] = count

for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(input()))
    result = click_count(N)
    print("#{} {}".format(tc, result))

