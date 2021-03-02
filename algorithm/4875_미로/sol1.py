import sys
sys.stdin = open("input.txt")

T = int(input())

def dfs(N, start, end):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[False for _ in range(N)] for _ in range(N)]
    stack = [start]

    while stack:
        v = stack.pop()
        if visited[v[0]][v[1]] == False:
            visited[v[0]][v[1]] = True
            for direction in range(4):
                x = v[0] + dr[direction]
                y = v[1] + dc[direction]
                if 0 <= x < N and 0 <= y < N and visited[x][y] == False and puzzle[x][y] == 0:
                    stack.append((x, y))
                elif 0 <= x < N and 0 <= y < N and visited[x][y] == False and puzzle[x][y] == 3:
                    visited[x][y] = True
    if visited[end[0]][end[1]]:
        return 1
    else:
        return 0

for tc in range(1, T+1):
    N = int(input())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, ' '.join(input()).split())))

    # start 위치 찾기
    for i in range(N):
        if puzzle[i].count(2) == 1:
            for j in range(N):
                if puzzle[i][j] == 2:
                    start = (i, j)
        if puzzle[i].count(3) == 1:
            for j in range(N):
                if puzzle[i][j] == 3:
                    end = (i, j)

    result = dfs(N, start, end)
    print("#{} {}".format(tc, result))

