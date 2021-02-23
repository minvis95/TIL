import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    num_text, text = list(input().split())

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

    print("#{} {}".format(tc, ''.join(stack)))

