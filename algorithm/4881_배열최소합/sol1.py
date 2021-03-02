import sys
sys.stdin = open("input.txt")

T = int(input())

def dfs(row, sub_sum):
    global min_result
    if row == N:
        if sub_sum < min_result:
            min_result = sub_sum
        return
    if sub_sum >= min_result:
        return
    for col in range(N):
        if visited[col] == False:
            visited[col] = True
            dfs(row + 1, sub_sum + numbers[row][col])
            visited[col] = False

for tc in range(1, T+1):
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(list(map(int, input().split())))
    visited = [False] * N
    min_result = 9*N
    dfs(0, 0)
    print("#{} {}".format(tc, min_result))

