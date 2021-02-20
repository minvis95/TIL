import sys
sys.stdin = open("input.txt")

T = int(input())
# Last in First out
def count_iron(text):
    current = []
    count = 0
    for i in range(len(text)):
        if text[i] == '(':
            current.append(text[i])
        elif text[i] == ')':
            if text[i-1] == '(':
                current.pop()
                count += len(current)
            # 끝부분 추가를 위해 ex (((()()))) 에서 )))이 부분때무누에
            else:
                current.pop()
                count += 1
    return count


for tc in range(1, T+1):
    text = list(input())
    result = count_iron(text)
    print("#{} {}".format(tc, result))

