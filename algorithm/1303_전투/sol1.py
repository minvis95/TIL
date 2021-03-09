import sys
sys.stdin = open("input.txt")

T = 1

def bfs(x, y, person):
    global count
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = True

    for direction in range(4):
        xx = x + dx[direction]
        yy = y + dy[direction]
        if 0 <= xx < M and 0 <= yy < N and mini_map[xx][yy] == person and visited[xx][yy] == False:
            bfs(xx, yy, person)
            count += 1

for tc in range(1, T+1):
    N, M = map(int, input().split())
    mini_map = []
    for _ in range(M):
        mini_map.append(input())
    # 방문기록 False로 초기화
    visited = [[False for _ in range(N)] for _ in range(M)]
    my_team = 0
    enemy = 0

    # 모든 원소 조사
    for i in range(M):
        for j in range(N):
            count = 1
            if visited[i][j]:
                continue
            else:
                # 해당 원소로부터 연쇄반응
                if mini_map[i][j] == 'W':
                    bfs(i, j, 'W')
                    my_team += count**2
                else:
                    bfs(i, j, 'B')
                    enemy += count**2

    print('{} {}'.format(my_team, enemy))


