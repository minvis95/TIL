import sys
from collections import deque
sys.stdin = open("input.txt")

T = 10

def bfs(v):
    visited = [False] * 101
    Q = deque([v])
    # bfs를 사용하여 각각의 노드의 깊이 측정
    depth = [0]*101
    while Q:
        v = Q.popleft()
        if not visited[v]:
            visited[v] = True
            for w in edge_list[v]:
                # w가 Q에 또 저장되면서 depth가 증가할 수 있으므로 Q에 들어있는지 확인해야함
                if visited[w] == False and w not in Q:
                    Q.append(w)
                    depth[w] = depth[v] + 1

    # 노드의 깊이가 가장 높으면서 index도 가장 높은거 찾고 return
    max_depth, index = 0, 0
    for i in range(101):
        if max_depth <= depth[i]:
            max_depth = depth[i]
            index = i
    return index

for tc in range(1, T+1):
    num, start = map(int, input().split())
    input_list = list(map(int, input().split()))

    edge_list = [[] for _ in range(101)]
    for i in range(num//2):
        if input_list[2*i+1] not in edge_list[input_list[2*i]]:
            edge_list[input_list[2*i]].append(input_list[2*i+1])
    result = bfs(start)
    print("#{} {}".format(tc, result))

