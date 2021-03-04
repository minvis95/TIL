import sys
sys.stdin = open("input.txt")

T = int(input())

'''
숫자 1부터 시작해서 숫자 1의 상하좌우 방들 중 2가 있냐?
있으면 visited[1] = True를 취해
이렇게 모든 숫자를 다 해버려
True로 쭈욱 연결된 것중 가장 긴 것들중에서 가장 작은 번호의 방이 답임
'''
def max_move(N):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [False] * (N*N + 1)
    # row
    for i in range(N):
        # column
        for j in range(N):
            for direction in range(4):
                x = i + dr[direction]
                y = j + dc[direction]
                if 0 <= x < N and 0 <= y < N and room[i][j] + 1 == room[x][y]:
                    visited[room[i][j]] = True
                    # 하나 밖에 존재 안하니깐
                    break

    min_room, max_length = 0, 0
    length = 1
    # 숫자를 돌려
    # N = 3이라면 9부터 1까지
    for number in range(N**2, -1, -1):
        if visited[number]:
            length += 1
        else:
            # max_length와 max_room 갱신, '='은 가장 긴것들중 가장 작은 번호를 원하기때문에
            if max_length <= length:
                max_length = length
                # 현재 i에서 false니깐 앞에 숫자까지만 연결되어있다는 것이지
                min_room = number + 1
            length = 1
    return min_room, max_length


for tc in range(1, T+1):
    N = int(input())
    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))
    result1, result2 = max_move(N)
    print("#{} {} {}".format(tc, result1, result2))

