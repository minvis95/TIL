import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    pizza = [(i + 1, temp[i]) for i in range(M)]
    in_pizza = pizza[:N]
    out_pizza = pizza[N:]
    while len(in_pizza) != 1:
        num, cheese = in_pizza.pop(0)
        cheese //= 2
        if cheese:
            in_pizza.append((num, cheese))
        else:
            if out_pizza:
                in_pizza.append(out_pizza.pop(0))

    print("#{} {}".format(tc, in_pizza[0][0]))

