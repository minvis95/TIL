import sys
sys.stdin = open("input.txt")

T = int(input())

def Palindrome(N, M, text_list):
    result = ''
    # N*N 메트릭스이므로 가로 세로 따로따로 for문을 할 필요는 없네
    for i in range(N):
        # 가로
        for j in range(N - M + 1):
            for k in range(M//2):
                if text_list[i][j+k] != text_list[i][j + M - 1 - k]:
                    break
            else:
                for x in range(M):
                    result += text_list[i][j+x]
                return result
        # 세로
        for j in range(N - M + 1):
            for k in range(M // 2):
                if text_list[j + k][i] != text_list[j + M - 1 - k][i]:
                    break
            else:
                for x in range(M):
                    result += text_list[j + x][i]
                return result

for tc in range(1, T+1):
    N, M = map(int, input().split())
    text_list = [list(input()) for _ in range(N)]

    result = Palindrome(N, M, text_list)

    print("#{} {}".format(tc, result))

