import sys
sys.stdin = open("input.txt")

T = int(input())

def possibility(depth, left, right, remainder_weights, N):
    global count
    # 끝까지 온경우
    if depth == N:
        count += 1
        return

    # 가지치기
    if left > right + remainder_weights:
        count += factorial(N - depth) * (2 ** (N - depth))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            # 왼쪽부터
            possibility(depth + 1, left + weights[i], right, remainder_weights - weights[i], N)
            # 오른쪽
            if right + weights[i] <= left:
                possibility(depth + 1, left, right + weights[i], remainder_weights - weights[i], N)
            visited[i] = False

def factorial(n):
    # base_case
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    count = 0
    visited = [False for _ in range(N)]
    possibility(0, 0, 0, sum(weights), N)
    print("#{} {}".format(tc, count))

