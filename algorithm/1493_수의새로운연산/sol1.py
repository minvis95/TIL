import sys
sys.stdin = open("input.txt")

T = int(input())

def new_sum(p, q):
    ## p와 q의 좌표 찾기
    # 큰수 찾기
    big_num = 0
    if p > q:
        big_num = p
    else:
        big_num = q

    default_val = 1
    p_di, q_di = 0, 0
    p_l = [1]*2
    q_l = [1]*2
    # 대각선 위치 찾기
    for y in range(1, big_num+1):
        default_val += y
        if default_val > p and p_di == 0:
            p_di = default_val - y
            p_l[1] = y
            re1 = y
        if default_val > q and q_di == 0:
            q_di = default_val - y
            q_l[1] = y
            re2 = y
    while p_di != p:
        if p_di < p:
            p_di += 1
            p_l[0] += 1
            p_l[1] -= 1
    while q_di != q:
        if q_di < q:
            q_di += 1
            q_l[0] += 1
            q_l[1] -= 1
    # p와 q의 좌표 합
    sum_l = [p_l[0]+q_l[0], p_l[1] + q_l[1]]
    # 좌표합의 숫자 찾기
    default_val = 1
    for i in range(1, re1+re2+1):
        default_val += i
    return default_val + sum_l[0]-1

for tc in range(1, T+1):
    p, q= map(int, input().split())
    result = new_sum(p, q)
    print("#{} {}".format(tc, result))

