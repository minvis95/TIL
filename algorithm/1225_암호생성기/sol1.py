import sys
from collections import deque
sys.stdin = open("input.txt")

T = 10
def encode(plain_text):
    i = 1
    while plain_text[0] - i > 0:
        plain_text.append(plain_text.popleft() - i)
        if i % 5:
            i = i + 1
        else:
            i = 1
    plain_text.popleft()
    plain_text.append(0)
for tc in range(1, T+1):
    test_case = int(input())
    plain_text = deque(map(int, input().split()))
    encode(plain_text)
    print("#{} ".format(test_case), end = '')
    print(*plain_text)
