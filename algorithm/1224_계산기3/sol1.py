import sys
sys.stdin = open("input.txt")

# in stack
def isp(num):
    if num == '(':
        return 0
    elif num == '*':
        return 2
    elif num == '+':
        return 1
# in coming
def icp(num):
    if num == '(':
        return 3
    elif num == '*':
        return 2
    elif num == '+':
        return 1
def first(numbers):
    stack = []
    result = ''
    for num in numbers:
        if num.isdigit():
            result += num
        elif num == ')':
            while stack[-1] != '(':
                result += stack.pop()
            # '(' pop시킨다.
            stack.pop()
        # + 또는 ( 또는 *일때
        else:
            if not stack:
                stack.append(num)
            else:
                while isp(stack[-1]) >= icp(num):
                    result += stack.pop()
                    if not stack:
                        break
                stack.append(num)
    # stack안에 있는것 다 빼기
    while stack:
        result += stack.pop()
    return second(' '.join(result).split())

def second(numbers):
    stack = []
    for i in range(len(numbers)):
        if numbers[i].isdigit():
            stack.append(numbers[i])
        else:
            number1, number2 = int(stack.pop()), int(stack.pop())
            if numbers[i] == '+':
                result = number2 + number1
            elif numbers[i] == '*':
                result = number2 * number1
            stack.append(str(result))
    return stack[0]
T = 10
for tc in range(1, T+1):
    length = int(input())
    numbers = ' '.join(input()).split()
    result = first(numbers)
    print("#{} {}".format(tc, result))

