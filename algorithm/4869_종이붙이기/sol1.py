import sys
sys.stdin = open("input.txt")

T = int(input())

def attach_paper(N):
    # base case
    if N == 1:
        return 1
    elif N == 2:
        return 3
    return attach_paper(N - 1) + (2 * attach_paper(N - 2))

for tc in range(1, T+1):
    N = int(input())
    result = attach_paper(N//10)
    print("#{} {}".format(tc, result))

