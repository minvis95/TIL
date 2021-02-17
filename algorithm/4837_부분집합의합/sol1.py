import sys
sys.stdin = open("input.txt")

T = int(input())

def subset_sum(N, K):
    N_list = []
    A = [i for i in range(1, 13)]

    for i in range(1<<12):
        N_list_list = []
        j_list = []
        cnt = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                j_list.append(j)
            if cnt > N:
                break
        else:
            if cnt == N:
                for j in j_list:
                    N_list_list.append(A[j])
                N_list.append(N_list_list)

    result = 0
    for subset in N_list:
        sum_subset = 0
        for i in subset:
            sum_subset += i
        if sum_subset == K:
            result += 1
    return result

for tc in range(1, T+1):
    N, K = map(int, input().split())

    result = 0
    result = subset_sum(N, K)

    print("#{} {}".format(tc, result))

