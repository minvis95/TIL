import sys
sys.stdin = open("input.txt")

T = int(input())

# 카드의 숫자와 장수 출력
def maximum_card(card_numbers):
    # 카드숫자의 count를 세기 위해 변수 세팅
    # 이때 idx는 카드의 숫자, value는 그 숫자의 개수이다.
    count_list = [0 for _ in range(0, 10)]

    # 카운트 센다.
    for number in card_numbers:
        count_list[number] += 1

    max_count = 0
    max_number = 0
    # 카드의 숫자와 그숫자의 개수를 받아와
    # enumerate 써보고 싶어서 썼음
    for idx, count in enumerate(count_list):
        # 개수가 같더라도 카드의 숫자는 다를 수 있으므로 '=' 추가
        if max_count <= count:
            # 갱신
            max_count = count
            # '= '등호가 들어가는 이유는 0번째 idx를 max_number에 넣기 위해
            if max_number <= idx:
                max_number = idx

    return max_number, max_count

for tc in range(1, T+1):
    # card <- 카드 몇장(N)
    card = input()
    # card_numbers <- 카드의 숫자 list(a1,a2,....aN)
    card_numbers = list(map(int, input()))

    result = maximum_card(card_numbers)
    print("#{} {} {}".format(tc, result[0], result[1]))

