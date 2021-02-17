import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    color1 = []
    color2 = []
    count = 0
    for _ in range(N):
        color_domain = []
        color_domain = list(map(int, input().split()))

        if color_domain[4] == 1:
            for i in range(color_domain[0], color_domain[2]+1):
                for j in range(color_domain[1], color_domain[3]+1):
                    if not [i, j] in color1:
                        color1.append([i, j])

        else:
            for i in range(color_domain[0], color_domain[2]+1):
                for j in range(color_domain[1], color_domain[3]+1):
                    if not [i, j] in color2:
                        color2.append([i, j])

    for red in color1:
        for blue in color2:
            if red == blue:
                count += 1
    print("#{} {}".format(tc, count))

