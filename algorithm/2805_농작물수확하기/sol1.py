import sys
sys.stdin = open("input.txt")

T = int(input())

def count_test(text, N):
    if N == 1:
        return text[0][0]

    middle = N // 2
    sum_line = 0
    for k in range(0, middle):
        if k == 0:
            sum_line += text[k][middle]
            continue
        sum_line += sum(text[k][middle - k:middle + k + 1])

    sum_line += sum(text[middle])

    for k in range(0, middle):
        if k == 0:
            sum_line += text[N - 1][middle]
            continue
        sum_line += sum(text[N - 1 - k][middle - k:middle + k + 1])

    return sum_line

for tc in range(1, T+1):
    N = int(input())
    text = []
    for _ in range(N):
        text.append(list(map(int, input())))
    # print(text)
    result = count_test(text, N)
    print("#{} {}".format(tc, result))

