import sys
from collections import deque
sys.stdin = open("input.txt")

def bfs(k, N, M):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = 0
    for i in range(N):
        for j in range(N):
            Q = deque()
            count = 0
            if mini_map[i][j]:
                count = 1
            visited = [[False for _ in range(N)] for _ in range(N)]
            visited[i][j] = True
            Q.append((i, j, 1))
            for c_k in range(2, k+1):
                while Q and Q[0][2] != c_k:
                    c_x, c_y, length = Q.popleft()
                    for direct in range(4):
                        x = c_x + dr[direct]
                        y = c_y + dc[direct]
                        if 0 <= x <= N-1 and 0 <= y <= N-1 and not visited[x][y]:
                            visited[x][y] = True
                            Q.append((x, y, length+1))
                            if mini_map[x][y]:
                                count += 1
                if count * M >= c_k**2 + (c_k-1)**2:
                    if count > result:
                        result = count
    return result


T = int(input())

T = 10
for tc in range(1, T+1):
    N, M = map(int, input().split())
    temp, mini_map = [], []
    house_count = 0
    # 집의 총 개수 구하기
    for _ in range(N):
        temp = list(map(int, input().split()))
        house_count += temp.count(1)
        mini_map.append(temp)
    # 최대 k구하기
    sum_M = house_count * M
    k = 1
    while k**2+(k-1)**2 <= sum_M:
        k += 1
    k -= 1

    result = bfs(k, N, M)
    if result:
        print("#{} {}".format(tc, result))
    else:
        print("#{} 1".format(tc))
