# BFS (Breadth First Search) : 너비 우선 탐색
# 최근접 경로를 구하기 위해서 사용됨
# ex. 페이스북에서 친구의 친구 추천, 네비게이션 등


vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertexList, edgeList)


def breadth_first_search(graph, start):
    vertexList, edgeList = graph
    visited = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visited:
                queue.insert(0, neighbor)
        visited.append(current)

    return visited


print(breadth_first_search(graphs, 0))