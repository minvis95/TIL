import sys
sys.stdin = open("input.txt")

M, N = map(int, input().split())

result = []

if M == 1:
    M += 1

if M == 2:
    M += 1
    result.append(2)

for number in range(M, N+1):
    for s_than_num in range(2, number):
        if number % s_than_num == 0:
            break
    else:
        result.append(number)

for i in range(len(result)):
    print(result[i])
