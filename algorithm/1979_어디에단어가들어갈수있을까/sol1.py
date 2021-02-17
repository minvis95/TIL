import sys
sys.stdin = open("input.txt")

T = int(input())
def solve_puzzle(N, K, puzzle):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 해당 칸이 검은색이면 다음 칸으로 continue
            if puzzle[i][j] == 0:
                continue
            # 상하좌우 하나씩 들어와
            for dir in range(4):
                # 반대방향으로 한칸이 검은색이 아니면 안되요~
                if puzzle[i-dr[dir]][j-dc[dir]] != 0:
                    continue
                # 정방향으로 1칸, 2칸, .., k-1칸이 일단 흰색이어야됌
                for num in range(1, K):
                    if puzzle[i+dr[dir]*num][j+dc[dir]*num] == 0:
                        break
                # 일단 다 자기포함해서 길이가 K만큼 흰색이야
                else:
                    # 근데 맨 마지막칸의 옆칸이 흰색이면?? 안되지.
                    # 따라서 검은색이면 카운트 증가
                    if puzzle[i+dr[dir]*K][j+dc[dir]*K] == 0:
                        cnt += 1
    # 매 칸마다 상하좌우를 다 조사하기때문에 K길이의 양 끝 칸은 무조건 cnt에 +1를 해준다.
    # 따라서 2로 나누어 주자
    # cnt는 무조건 짝수로 나올 수 밖에 없다.
    # ex) k가 3일때 1번째부터 3번째까지 흰색이면 반대로 3번째부터 1번째까지도 흰색이기에 나누기 2!
    return cnt//2

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = []
    # 겉테두리를 생성(겉테두리는 검은색이다)
    for i in range(N):
        if i == 0:
            puzzle.append([0]*(N+2))

        puzzle += [[0] + list(map(int, input().split())) + [0]]

        if i == N-1:
            puzzle.append([0]*(N+2))

    result = solve_puzzle(N, K, puzzle)
    print("#{} {}".format(tc, result))

