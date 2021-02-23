import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    text = input()

    stack = []
    top = -1
    for word in text:
        # 스택의 길이가 0이면 append
        if len(stack) == 0:
            stack.append(word)
            top += 1
        elif stack[top] != word:
            stack.append(word)
            top += 1
        else:
            stack.pop()
            top -= 1

    print("#{} {}".format(tc, len(stack)))

