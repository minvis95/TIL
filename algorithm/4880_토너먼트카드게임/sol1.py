import sys
sys.stdin = open("input.txt")

T = int(input())

def solution(person1, person2):
    v = people[person1]
    w = people[person2]

    if v == w:
        return person1
    else:
        if v == 1 and w == 2:
            return person2
        elif v == 1 and w == 3:
            return person1
        elif v == 2 and w == 1:
            return person1
        elif v == 2 and w == 3:
            return person2
        elif v == 3 and w == 1:
            return person2
        elif v == 3 and w == 2:
            return person1

def battle(start, end):
    # base case
    if start == end:
        return start
    person1 = battle(start, (start+end )// 2)
    person2 = battle((start+end )// 2 + 1, end)

    # 승자 인덱스 return
    return solution(person1, person2)
for tc in range(1, T+1):
    N = int(input())
    people = list(map(int, input().split()))
    result = battle(0, N - 1)
    print("#{} {}".format(tc, result + 1))

