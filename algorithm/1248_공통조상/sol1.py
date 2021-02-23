import sys
sys.stdin = open("input.txt")

def dfs(v, N):
    stack = []
    visited = [False] * (N + 1)
    stack.append(v)
    while len(stack):
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for w in edge_list[v]:
                if not visited[w]:
                    stack.append(w)
    return visited


def find_parent(x):
    # base case(최상위 루트 일때)
    if x == 1:
        return []
    for idx, value in enumerate(edge_list):
        if x in value:
            return [idx] + find_parent(idx)

T = int(input())
for tc in range(1, T+1):
    V, E, X, Y = map(int, input().split())
    input_list = list(map(int, input().split()))
    edge_list = [[] for _ in range(V + 1)]
    for i in range(E):
        start, end = input_list[2 * i], input_list[2 * i + 1]
        edge_list[start].append(end)

    # 공통 조상 구하기
    parent_list1 = find_parent(X)
    parent_list2 = find_parent(Y)

    parent = 0
    for i in parent_list1:
        for j in parent_list2:
            if i == j:
                parent = i
                break
        if parent:
            break
    result = dfs(parent, V)
    count = result.count(True)

    print("#{} {} {}".format(tc, parent, count))

