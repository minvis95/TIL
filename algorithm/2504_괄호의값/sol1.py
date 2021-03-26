import sys
sys.stdin = open("input.txt")

input_list = list(input())
stack = []
stack.append(input_list[0])
top = 0

for value in range(1, len(input_list)):
    if input_list[value] == '(':
        stack.append('(')
        top += 1
    elif input_list[value] == '[':
        stack.append('[')
        top += 1
    elif input_list[value] == ')':
        if stack[top] == '(':
            stack.pop()
            stack.append('2')
        else:
            m_sum = 0
            for i in range(top, -1, -1):
                if stack[i] == '(':
                    stack[i] = str(2 * m_sum)
                    break
                else:
                    if stack[i].isdigit():
                        m_sum += int(stack[i])
                        stack.pop()
                        top -= 1
                    else:
                        print(0)
                        exit(0)
    else:   # input_list[value] == ']'
        if stack[top] == '[':
            stack.pop()
            stack.append('3')
        else:
            m_sum = 0
            for i in range(top, -1, -1):
                if stack[i] == '[':
                    stack[i] = str(3 * m_sum)
                    break
                else:
                    if stack[i].isdigit():
                        m_sum += int(stack[i])
                        stack.pop()
                        top -= 1
                    else:
                        print(0)
                        exit(0)

result = 0
for i in range(len(stack)):
    result += int(stack[i])
print(result)