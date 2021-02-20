import sys
sys.stdin = open("input.txt")

T = int(input())

def read_col(text):
    count_list = [len(text[i]) for i in range(5)]
    M = max(count_list)
    result =''
    for i in range(M):
        for j in range(5):
            if count_list[j] != 0:
                count_list[j] -= 1
                result += text[j][i]
    return result

for tc in range(1, T+1):
    text = [list(input()) for _ in range(5)]
    result = read_col(text)
    print("#{} {}".format(tc, result))

