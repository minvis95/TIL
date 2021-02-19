import sys
sys.stdin = open("input.txt")

T = int(input())

def max_word_count(str1, str2):
    count_list = []

    for i in range(len(str1)):
        count = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count += 1
        else:
            count_list.append(count)
    return max(count_list)

for tc in range(1, T+1):
    str1, str2= input(), input()
    result = max_word_count(str1, str2)

    print("#{} {}".format(tc, result))

