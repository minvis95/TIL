import sys
sys.stdin = open("input.txt")

T = int(input())

def compare_strs(T, P):
    n, m = len(T), len(P)

    for i in range(n - m + 1):
        if T[0 + i:m + i] == P:
            return 1
    return 0


for tc in range(1, T+1):
    P = input()
    T = input()
    result = compare_strs(T, P)
    print("#{} {}".format(tc, result))

