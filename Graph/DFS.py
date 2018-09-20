# DFS (Depth First Search) 깊이 우선 탐색
# 체스에서 승리 요건을 검색하기 위해
# vertex : node
# edge : vertex 간의 연결
# adjacency : 한 vertex의 인접 vertex 목록

import unittest
from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)

    def isCyclicUtil(self, vertex, visited, stack):
        visited[vertex] = True
        stack[vertex] = True

        for neighbor in self.graph[vertex]:
            if visited[neighbor] == False:
                if self.isCyclicUtil(neighbor, visited, stack) == True:
                    return True
            elif stack[neighbor] == True:
                return True

        stack[vertex] = False
        return False

    def isCyclic(self):
        visited = [False] * self.vertices
        stack = [False] * self.vertices
        for node in range(self.vertices):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, stack) == True:
                    return True
        return False


def depth_first_search(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)

    return visitedVertex


class unit_test(unittest.TestCase):
    def test(self):
        vertexList = ['0', '1', '2', '3', '4', '5', '6']
        edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4), (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]
        graphs = (vertexList, edgeList)
        self.assertEqual([0, 2, 5, 4, 6, 1, 3],depth_first_search(graphs, 0))


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")