import sys
sys.stdin = open("input.txt")

T = 10

def max_len_abba(text):
    result = 1
    for i in range(100):
        for j in range(100):
            tmp = 0
            for end in range(99, j, -1):
                M = end - j + 1
                for k in range(M//2):
                    if text[i][j+k] != text[i][end-k]:
                        break
                else:
                    tmp = M
                    if M > result:
                        result = M
                if tmp == M:
                    break
            for end in range(99, j, -1):
                M = end - j + 1
                for k in range(M//2):
                    if text[j+k][i] != text[end-k][i]:
                        break
                else:
                    tmp = M
                    if M > result:
                        result = M
                if tmp == M:
                    break

    return result

for tc in range(1, T+1):
    no_need = input()
    text = [list(input()) for _ in range(100)]
    result = max_len_abba(text)
    print('#{} {}'.format(tc, result))