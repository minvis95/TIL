import sys
sys.stdin = open("input.txt")

def icp(word):
    if word == '+':
        return 1
def isp(word):
    if word == '+':
        return 1

def postfix(text):
    stack = []
    top = -1
    result = []
    for word in text:
        if word == '+':
            if len(stack) == 0:
                stack.append(word)
                top += 1
                continue
            while isp(stack[top]) >= icp(word):
                result.append(stack.pop())
                top -= 1
                if top == -1:
                    break
            stack.append(word)
            top += 1
        else:
            result.append(word)
    result.append(stack[0])
    print(result)
    return result

T = int(input())
T = 1
for tc in range(1, T+1):
    text = input()
    result = postfix(text)

    print("#{} ".format(tc, ))

