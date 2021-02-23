import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    text = input()

    stack = []
    top = -1
    for word in text:
        if word == '(' or word == '{':
            stack.append(word)
            top += 1
        elif word == ')':
            if len(stack) == 0:
                print("#{} 0".format(tc))
                break
            if stack[top] == '(':
                stack.pop()
                top -= 1
            else:
                print("#{} 0".format(tc))
                break
        elif word == '}':
            if len(stack) == 0:
                print("#{} 0".format(tc))
                break
            if stack[top] == '{':
                stack.pop()
                top -= 1
            else:
                print("#{} 0".format(tc))
                break
    else:
        if len(stack) == 0:
            print("#{} 1".format(tc))
        else:
            print("#{} 0".format(tc))