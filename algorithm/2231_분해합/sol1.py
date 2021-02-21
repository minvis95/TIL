N = int(input())
# N = 256

result = 0
# 1부터 N까지 모든 값을 조사. Then 가장 작은 생성자가 먼저 출력되고 break됌
for i in range(1, N + 1):
    # 리스트로 만듬(각 자리수)
    i_list = [int(i) for i in str(i)]
    # 각자리수의 합과 원래값을 더함
    result = sum(i_list) + i
    # 같냐?
    if result == N:
        print(i)
        # 245
        break
    # 다 조사해봤는데 없으니깐 0 출력
    if N == i:
        print(0)
        break
