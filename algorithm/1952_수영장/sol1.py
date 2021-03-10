import sys
sys.stdin = open("input.txt")

T = int(input())

def find_min(index, m_sum):
    global min_value
    # 중간값이 현재 min_value보다 큰경우는 return!
    if min_value < m_sum:
        return
    # 끝까지 온경우
    if index > 11:
        if min_value > m_sum:
            min_value = m_sum
        return
    # 1일 이용권
    find_min(index+1, m_sum+price[0]*plan[index])
    # 1달 이용권
    find_min(index+1, m_sum+price[1])
    # 3달 이용권
    find_min(index+3, m_sum+price[2])

for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_value = price[3]
    find_min(0, 0)
    print("#{} {}".format(tc, min_value))

