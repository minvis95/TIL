import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # A, B 부딪히는 시간 = 속력분의 거리
    hello_train = D / (A + B)
    # 그 시간 만큼 파리는 움직일 것이다.
    result = F * hello_train

    print("#{} {:.6f}".format(tc, result))

