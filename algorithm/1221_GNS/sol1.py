import sys
sys.stdin = open("input.txt")

T = int(input())
def sort_string(N, string_list):
    number_dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9,}
    number_list = []
    for i in range(N):
        number_list.append(number_dict[string_list[i]])
    number_list.sort()
    for i in range(N):
        for j in number_dict.keys():
            if number_dict[j] == number_list[i]:
                number_list[i] = j
    return number_list
for tc in range(1, T+1):

    no_need, N = input().split()
    N = int(N)
    string_list = list(map(str, input().split()))
    result = []
    result = sort_string(N, string_list)
    print("#{}".format(tc))
    for i in range(N):
        print(result[i], end=' ')
    print()
