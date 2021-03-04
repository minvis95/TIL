import sys
from collections import deque
sys.stdin = open("input.txt")

T = int(input())

def bfs(v, end):
    visited = [False] * 51
    depth = [0] * 51
    Q = deque([v])

    while Q:
        v = Q.popleft()
        if not visited[v]:
            visited[v] = True
            for w in edge_list[v]:
                if not visited[w] and w not in Q:
                    Q.append(w)
                    depth[w] = depth[v] + 1
    return depth[end]

for tc in range(1, T+1):
    # 노드의 개수 V, 간선의 개수 E
    V, E = map(int, input().split())
    edge_list = [[] for _ in range(51)]
    for _ in range(E):
        start, end = map(int, input().split())
        edge_list[start].append(end)
        edge_list[end].append(start)

    start, end = map(int, input().split())

    if tc == 2:
        print(edge_list)
        print(start, end)
    result = bfs(start, end)
    print("#{} {}".format(tc, result))

