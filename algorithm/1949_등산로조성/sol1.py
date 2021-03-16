import sys
sys.stdin = open("input.txt")

T = int(input())

def solution(c_x, c_y, length, check):
    global max_result, K
    max_result = max(max_result, length)
    for direct in range(4):
        x = c_x + dx[direct]
        y = c_y + dy[direct]
        if 0 <= x <= N-1 and 0 <= y <= N-1:
            if not visited[x][y]:
                if mini_map[x][y] < mini_map[c_x][c_y]:
                    visited[x][y] = True
                    solution(x, y, length+1, check)
                    visited[x][y] = False
                elif not check and mini_map[x][y] - K < mini_map[c_x][c_y]:
                    check = True
                    for num in range(1, K+1):
                        if mini_map[x][y] - num < mini_map[c_x][c_y]:
                            number = num
                            break
                    mini_map[x][y] -= number
                    visited[x][y] = True
                    solution(x, y, length+1, check)
                    visited[x][y] = False
                    mini_map[x][y] += number
                    check = False
for tc in range(1, T+1):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    N, K = map(int, input().split())
    mini_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    max_place = []
    max_result = 0
    max_value = []
    for mini in mini_map:
        max_value.append(max(mini))
    temp = max(max_value)
    for x in range(N):
        for y in range(N):
            if mini_map[x][y] == temp:
                max_place.append((x, y))
    for place in max_place:
        visited[place[0]][place[1]] = True
        solution(place[0], place[1], 1, False)
        visited[place[0]][place[1]] = False
    print("#{} {}".format(tc, max_result))

