import sys
sys.stdin = open("input.txt")

T = 10

def count_palindrome(M, text):
    count = 0

    for i in range(8):
        for j in range(0, 8 - M + 1):
            for k in range(M // 2):
                if text[i][j+k] != text[i][j + M - 1 - k]:
                    break
            else:
                count += 1

            for k in range(M // 2):
                if text[j + k][i] != text[j + M - 1 - k][i]:
                    break
            else:
                count += 1
    return count

for tc in range(1, T+1):
    M = int(input())
    text = [list(input()) for _ in range(8)]

    result = count_palindrome(M, text)
    print("#{} {}".format(tc, result))

