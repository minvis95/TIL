import sys
sys.stdin = open("input.txt")

T = int(input())

# 순서 중요하지않아 조합
def min_sum(h_sum, s, e, B):
    global result

    if result > h_sum >= B:
        result = h_sum
        return

    for i in range(s, e):
        min_sum(h_sum + Hs[i], i+1, e, B)


for tc in range(1, T+1):
    N, B = map(int, input().split())
    Hs = list(map(int, input().split()))
    result = sum(Hs)
    min_sum(0, 0, N, B)

    print("#{} {}".format(tc, result - B))

