import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    test_case, G = map(int, input().split())
    input_list = list(map(int, input().split()))

    # 인접 리스트
    edge_list = [[] for _ in range(100)]
    for i in range(G):
        start, end = input_list[2 * i], input_list[2 * i + 1]
        edge_list[start].append(end)

    # DFS
    stack = []
    visited = [False for _ in range(100)]
    stack.append(0)
    while len(stack):
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for w in edge_list[v]:
                if not visited[w]:
                    stack.append(w)
    if visited[99]:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))