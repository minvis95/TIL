import sys
sys.stdin = open("input.txt")

T = int(input())
T = 1
def search(N):
    visited = [[False for _ in range(N)] for _ in range(N)]
    result = []
    for row in range(N):
        for col in range(N):
            if visited[row][col] == False and numbers[row][col] != 0:
                visited[row][col] = True
                i, j = 1, 1
                while row + i < N and numbers[row+i][col] != 0:
                    i += 1
                while col + j < N and numbers[row][col+j] != 0:
                    j += 1
                result.append([i, j])
                for k in range(i):
                    for l in range(j):
                        visited[row+k][col+l] = True
    for i in range(len(result)):
        result[i].append(result[i][0] * result[i][1])

for tc in range(1, T+1):
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(list(map(int, input().split())))

    count, result = search(N)

    print("#{} {} ".format(tc, count), end='')
    for i in range(len(result)):
        print("{} ".format(result[i]), end='')
    print()

