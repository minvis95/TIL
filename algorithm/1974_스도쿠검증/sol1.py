import sys
sys.stdin = open("input.txt")

T = int(input())

def matrix(text):
    # 가로 검사
    for i in range(0, 9):
        for num in range(1, 10):
            if text[i].count(num) > 1:
                return 0

    # 세로 검사
    for i in range(0, 9):
        temp = []
        for j in range(0, 9):
            temp.append(text[j][i])
        for num in range(1, 10):
            if temp.count(num) > 1:
                return 0

    # 3*3 검사
    for x in range(0, 3):
        for k in range(0, 3):
            temp = []
            for i in range(0, 3):
                for j in range(0, 3):
                    temp.append(text[i + 3 * x][j + 3 * k ])

            for num in range(1, 10):
                if temp.count(num) > 1:
                    return 0
    return 1

for tc in range(1, T+1):
    text = []
    for _ in range(9):
        text.append(list(map(int, input().split())))

    result = matrix(text)
    print("#{} {}".format(tc, result))

