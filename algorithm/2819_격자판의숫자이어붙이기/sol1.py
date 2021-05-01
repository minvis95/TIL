import sys
sys.stdin = open("input.txt")

T = int(input())

def calculate(count, s, e, current_value):
    global result

    current_value += num_map[s][e]

    if count == 0:
        result.add(current_value)
        return

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for direct in range(4):
        x = s + dx[direct]
        y = e + dy[direct]
        if 0 <= x <= 3 and 0 <= y <= 3:
            calculate(count-1, x, y, current_value)

for tc in range(1, T+1):
    num_map = [input().split() for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            current_value = ''
            calculate(6, i, j, current_value)
    print("#{} {}".format(tc, len(result)))

