import sys
sys.stdin = open("input.txt")


def dfs(index, count):
    global min_value

    # 안뽑는 것으로 끝까지 간 경우
    # ex. when N=6, then TFFFFF or TTFFFF or FFFFFF
    # if FFFTTT이면? -> 이미 TTTFFF에서 계산하였기에 return해도 상관없음
    if index == N:
        return

    # 가지치기
    # T를 3개 뽑았을 경우
    if count == N//2:
        start, link = 0, 0
        # ex. visited -> TFTFTF일 경우 0번과 2번, 0번과 4번-> i증가시키고 1번과 3번, 1번과 5번
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                if not visited[i] and not visited[j]:
                    link += S[i][j]
        min_value = min(min_value, abs(start - link))
        return

    # 뽑고
    visited[index] = True
    # 뽑으면 count증가 and 다른 사람 뽑을지 말지 고르러 index 증가
    dfs(index+1, count+1)
    # 안뽑고
    visited[index] = False
    # 안뽑았으니깐 count 그대로
    dfs(index+1, count)

T = 3

for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    min_value = 20*20*100
    dfs(0, 0)
    print("{}".format(min_value))

