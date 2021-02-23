import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    num_text = int(input())
    text = list(input())

    stack = []
    top = -1
    for word in text:
        if len(stack) == 0:
            stack.append(word)
            top += 1
        elif word == '(' or word == '[' or word == '{' or word == '<':
            stack.append(word)
            top += 1
        else:
            if len(stack) == 0:
                print("#{} 0".format(tc))
                break
            if word == ')':
                if stack[top] == '(':
                    stack.pop()
                    top -= 1
                else:
                    print("#{} 0".format(tc))
                    break
            elif word == ']':
                if stack[top] == '[':
                    stack.pop()
                    top -= 1
                else:
                    print("#{} 0".format(tc))
                    break
            elif word == '}':
                if stack[top] == '{':
                    stack.pop()
                    top -= 1
                else:
                    print("#{} 0".format(tc))
                    break
            elif word == '>':
                if stack[top] == '<':
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