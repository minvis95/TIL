import sys
sys.stdin = open("input.txt")

T = int(input())
def calculate(numbers):
    flag = 0
    stack = []
    for i in range(len(numbers) - 1):
        if numbers[i].isdigit():
            stack.append(numbers[i])
        else:
            try:
                number1, number2 = int(stack.pop()), int(stack.pop())
                if numbers[i] == '+':
                    result = number2 + number1
                elif numbers[i] == '-':
                    result = number2 - number1
                elif numbers[i] == '*':
                    result = number2 * number1
                elif numbers[i] == '/':
                    result = number2 // number1
                stack.append(str(result))
            except:
                flag = 1
    if flag == 0 and len(stack) == 1:
        return stack[0]
    elif flag == 1 or len(stack) > 1:
        return 'error'

for tc in range(1, T+1):
    numbers = input().split()
    result = calculate(numbers)
    print("#{} {}".format(tc, result))

