import sys
from collections import deque
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q= deque(map(int, input().split()))
    Q.rotate(-M)
    print("#{} {}".format(tc, Q[0]))

