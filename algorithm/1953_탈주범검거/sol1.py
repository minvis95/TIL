import sys
from collections import deque
sys.stdin = open("input.txt")

T = int(input())

def what_tunnel(x, y):
    if puzzle[x][y] == 1:
        return tunnel_one
    elif puzzle[x][y] == 2:
        return tunnel_two
    elif puzzle[x][y] == 3:
        return tunnel_three
    elif puzzle[x][y] == 4:
        return tunnel_four
    elif puzzle[x][y] == 5:
        return tunnel_five
    elif puzzle[x][y] == 6:
        return tunnel_six
    elif puzzle[x][y] == 7:
        return tunnel_seven
    else:
        return []
def solution(count):
    # 상으로부터 시계방향
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    # Q 이용
    Q = deque()
    Q.append((R, C, count))
    while Q:
        # print(Q)
        v = Q.popleft()
        if not visited[v[0]][v[1]] and v[2] != 0:
            visited[v[0]][v[1]] = True
            c_tunnel = what_tunnel(v[0], v[1])
            for direct in c_tunnel:
                x = v[0] + dx[direct]
                y = v[1] + dy[direct]
                if 0 <= x <= N-1 and 0 <= y <= M-1 and not visited[x][y] and (direct+4)%8 in what_tunnel(x, y):
                    Q.append((x, y, v[2] - 1))
    result = 0
    for visite in visited:
        result += visite.count(True)
    return result

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    # 뚫려있는 곳 True : 상부터 시계방향으로
    tunnel_one = [0, 2, 4, 6]
    tunnel_two = [0, 4]
    tunnel_three = [2, 6]
    tunnel_four = [0, 2]
    tunnel_five = [2, 4]
    tunnel_six = [4, 6]
    tunnel_seven = [0, 6]
    result = solution(L)
    print("#{} {}".format(tc, result))

