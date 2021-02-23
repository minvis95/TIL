import sys
sys.stdin = open("input.txt")

# 지향 그래프이며 인접행렬과 인접리스트 둘다 표현하는 연습을 해보자
T = int(input())


for tc in range(1, T+1):
    # V개의 노드(꼭짓점, vertex), E개의 간선(edge, line, 변)
    V, E = list(map(int, input().split()))

    ## 인접 리스트
    edge_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        start, end = map(int, input().split())
        edge_list[start].append(end)

    S, G = map(int, input().split())

    visited = [False] * (V + 1)
    stack = [S]
    # 스텍에 하나라도 있다면 반복문 돌아
    while stack:
        v = stack.pop()
        # 방문하지 않았을 경우
        if not visited[v]:
            visited[v] = True
            # v노드와 연결된 모든 노드를 반복
            for w in edge_list[v]:
                # 방문을 안한 노드라면
                if not visited[w]:
                    stack.append(w)
    result = 1 if visited[G] else 0

    print("#{} {}".format(tc, result))

    ## 인접행렬
    # edge_matrix = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    # for _ in range(E):
    #     s, e = map(int, input().split())
    #     edge_matrix[s][e] = 1
    # print(edge_matrix)
    # S, G = map(int, input().split())
    # print(S, G)
