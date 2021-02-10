import sys
sys.stdin = open("input.txt")

T = int(input())

def fz(number):
    mod_list = [2, 3, 5, 7, 11]
    count_list = [0]*5

    for idx in range(len(mod_list)):
        while number % mod_list[idx] == 0:
            number //= mod_list[idx]
            count_list[idx] += 1
    return count_list

for tc in range(1, T+1):
    number = int(input())
    result = fz(number)

    print("#{} {}".format(tc, ' '.join(map(str, result))))

