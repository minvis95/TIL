import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, Q = tuple(map(int,input().split()))
    N_boxes = [0]*(N+1)
    Q_ith_list = [0]
    for _ in range(Q):
        Q_ith_list.append(list(map(int,input().split())))

    for i in range(1, Q+1):
        for j in range(Q_ith_list[i][0], Q_ith_list[i][1]+1):
            N_boxes[j] = i

    print("#{} {}".format(tc, ' '.join(map(str, N_boxes[1:]))))

