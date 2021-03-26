import sys
sys.stdin = open("input.txt")

def dfs(count, number):
    global result, result_list
    stack.append(number)
    if result <= count:
        return
    # count가 더 적으면서 숫자 1이 나올 때
    if stack[-1] == 1:
        result_list = []
        result = count
        result_list.extend(stack)
        return
    # 1번
    if stack[-1] % 3 == 0:
        dfs(count+1, number//3)
        stack.pop()
    # 2번
    if stack[-1] % 2 == 0:
        dfs(count+1, number//2)
        stack.pop()
    # 3번
    dfs(count+1, number-1)
    stack.pop()

n = int(input())
result = 1000000
result_list = []
stack = []
dfs(0, n)
print(result)
print(*result_list)
