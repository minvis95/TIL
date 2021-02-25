# N = 4
# numbers = [3, 5, 2, 7]

N = int(input())
numbers = list(map(int, input().split()))

# index가 쌓이는 변수
# 내림 차순으로 쌓이다가 없어지고 쌓이고 없어지고 함
stack = []
# numbers라는 list안에 i번째에 있는 원소의 오큰수 넣는 공간
check = [-1] * N

stack.append(0)
for idx, number in enumerate(numbers):
    # stack이 비어있으면 전 원소, 전전 원소,...등등은 현재 원소를 오큰수로 생각
    while stack and numbers[stack[-1]] < number:
        # 위에 조건 만족한거니 바로 check에다 대입
        check[stack[-1]] = number
        # 끝난건 팝
        stack.pop()

    stack.append(idx)

for i in range(N):
    print(check[i], end=' ')
