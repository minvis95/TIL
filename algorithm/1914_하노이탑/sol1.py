def hanoi(x, y, z, N):
    # base case
    if N == 1:
        print('{} {}'.format(x, z))
        return
    # N-1개를 1번째에서 2번째로 보내
    hanoi(x, z, y, N - 1)
    # 1번째에 있는 1개를 3번째로 보내
    hanoi(x, y, z, 1)
    # 2번째에 있는 N - 1개를 3번째로 보내
    hanoi(y, x, z, N - 1)

N = int(input())

print((2**N) - 1)
if N <= 20:
    hanoi(1, 2, 3, N)
