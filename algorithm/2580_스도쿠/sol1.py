import sys
sys.stdin = open("input.txt")

T = 1

def solution(count):
    # 숫자는 index로 따졌을 때 0~80까지 총 81개가 있다.
    if count == 81:
        for p in puzzle:
            print(*p)
        sys.exit(0)

    x, y = count // 9, count % 9
    if puzzle[x][y] == 0:
        for i in range(1, 10):
            # i 숫자가 모든 행과 열 box에 없으면 그값을 일단 넣어보고 다음 0을 찾아서 가봐
            # 만약에 다음 0에서 1~9숫자가 행,열,box에 다 존재해 그러면 return None이 되서 부모 노드로 돌아감
            # 부모 노드에서 모든 행과 열 box에 없는 다른 i숫자를 찾아
            if row[x][i] == False and col[y][i] == False and box[x // 3 * 3 + y // 3][i] == False:
                puzzle[x][y] = i
                row[x][i], col[y][i], box[x // 3 * 3 + y // 3][i] = True, True, True
                solution(count + 1)
                row[x][i], col[y][i], box[x // 3 * 3 + y // 3][i] = False, False, False
                puzzle[x][y] = 0
    else:
        solution(count + 1)

for tc in range(1, T+1):
    puzzle = list(list(map(int, input().split())) for _ in range(9))

    # 행, 열, box는 9개가 있고 각각 숫자 1~9의 방문기록을 False로 설정
    row = [[False for _ in range(10)] for _ in range(9)]
    col = [[False for _ in range(10)] for _ in range(9)]
    box = [[False for _ in range(10)] for _ in range(9)]

    # 초기화 -> 0이아닌 값이 들어있으면 True로 바꿔줌
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                row[i][puzzle[i][j]] = True
                col[j][puzzle[i][j]] = True
                box[i // 3 * 3 + j // 3][puzzle[i][j]] = True
    solution(0)

