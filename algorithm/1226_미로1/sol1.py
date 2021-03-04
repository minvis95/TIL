import sys
sys.stdin = open("input.txt")
from collections import deque


def solution():
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[False for _ in range(16)] for _ in range(16)]
    Q = deque()
    Q.append((1, 1))
    while Q:
        v = Q.popleft()
        if not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = True
            for direction in range(4):
                x = v[0] + dr[direction]
                y = v[1] + dc[direction]
                if 0 <= x < 16 and 0 <= y < 16 and visited[x][y] == False and puzzle[x][y] == 0 or puzzle[x][y] == 3:
                    Q.append((x, y))

    if visited[13][13]:
        return 1
    else:
        return 0

T = 10
for tc in range(1, T+1):
    test_case = int(input())
    puzzle = []
    for _ in range(16):
        puzzle.append(list(map(int, ' '.join(input()).split())))
    result = solution()
    print("#{} {}".format(tc, result))

