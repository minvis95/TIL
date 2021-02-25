import sys
sys.stdin = open("input.txt")

T = int(input())

def bubble_sort(N, schedule):
    for i in range(N - 1 , 0, -1):
        for j in range(i):
            if schedule[j] > schedule[j + 1]:
                schedule[j], schedule[j + 1] = schedule[j + 1], schedule[j]

def mission(M, K):
    max_schedule = schedule[-1]
    current = 0
    for second in range(1, max_schedule + 1):
        if second % M == 0:
            current += K
        while second == schedule[0]:
            current -= 1
            schedule.pop(0)
            if current < 0:
                return 'Impossible'
            if len(schedule) == 0:
                return 'Possible'
    # schedule 최대 원소 < M 일 경우
    return 'Impossible'

for tc in range(1, T+1):
    # N명의 손님, 진기 M초에 K개 만들어
    N, M, K = map(int, input().split())
    schedule = list(map(int, input().split()))
    bubble_sort(N, schedule)

    result = mission(M, K)
    print("#{} {}".format(tc, result))

