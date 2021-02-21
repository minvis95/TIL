import sys
sys.stdin = open("input.txt")

T = int(input())

def game_winner(N):
    # When N = 1, then Bob승리 N =2, 3은 Alice 승
    if N == 1:
        return 'Bob'
    elif N == 2:
        return 'Alice'
    elif N == 3:
        return 'Alice'
    # 깊이 계산 Alice로 인해서 결정되는 깊이인지 Bob으로 인해서 결정되는 깊이인지 판단
    depth = 0
    while N > (0b10<<depth):
        depth += 1
    # 마지막에 N과 비교될 숫자임
    M = 1
    # line = 'Alice'
    # Alice는 N보다 작거나 같게 하기위해 2만 곱할 것이다.
    if depth % 2 == 1:
        human1 = 'Alice'
        human2 = 'Bob'
        for i in range(depth):
            # Bob의 차례
            if i % 2 == 1:
                M = (M*2) + 1
            # Alice의 차례
            else:
                M = (M*2)
    # line = 'Bob'
    # Bob은 N보다 작거나 같게 하기위해 2만 곱할 것이다.
    else:
        human1 = 'Bob'
        human2 = 'Alice'
        for i in range(depth):
            if i % 2 == 1:
                M = (M*2)
            else:
                M = (M*2) + 1
    if M <= N:
        return human1
    else:
        return human2

for tc in range(1, T+1):
    N = int(input())
    result = game_winner(N)
    print("#{} {}".format(tc, result))

