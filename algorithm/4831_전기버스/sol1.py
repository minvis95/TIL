import sys
sys.stdin = open("input.txt")

T = int(input())

def bus(numbers, charging_nod):
    # 버스의 현재 위치를 확인하기
    pivot = 0
    # 현재 충전소 몇번 들렸니?
    count = 0

    # 현재 위치에서 K를 더하더라도 종점보다 작아? 그러면 go
    while pivot + numbers[0] < numbers[1]:
        # 최소한으로 하기 위해 K, K-1, K-2,...,1 순으로 움직였을때 충전소 있는지 확인
        for move in range(numbers[0], 0, -1):
            # 충전소가 있네?
            if pivot + move in charging_nod:
                # 현재위치에서 move만큼 이동해
                pivot += move
                # 카운트 증가
                count += 1
                break
        # 충전소가 없네ㅠ 그러면 더이상 나는 못가
        else:
            return 0
    return count

for tc in range(1, T+1):
    # K(이정도 갈수있어), N(여기가 종점), M(충전소 개수)
    numbers = list(map(int, input().split()))
    # 충전소 어디 위치해 있는지 가져와
    charging_nod = list(map(int, input().split()))
    # 충전소 몇번들리는지 체크
    result = bus(numbers, charging_nod)

    print("#{} {}".format(tc, result))

