def dfs(graph, start, visited, parent, length, min_length):
    visited[start] = True

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, start, length + 1, min_length)
        elif neighbor != parent:
            min_length = min(min_length, length + 1)

    return min_length


def min_cycle_length(graph):
    n = len(graph)
    min_length = float('inf')
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            min_length_in_component = dfs(graph, i, visited, -1, 0,
                                          float('inf'))
            min_length = min(min_length, min_length_in_component)

    return min_length


def generateAdjointGrph(list, k):
    # 构建邻接表
    graph = [[] for _ in range(k)]
    for edge in list:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    print(graph)
    return graph


# print(min_cycle_length(generateGraph([[1, 2], [2, 3], [3, 1]], 3)))
print(min_cycle_length(generateAdjointGrph([[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]], 7)))
