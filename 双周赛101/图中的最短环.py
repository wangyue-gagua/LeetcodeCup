""" 现有一个含 n 个顶点的 双向 图，每个顶点按从 0 到 n - 1 标记。图中的边由二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示顶点 ui 和 vi 之间存在一条边。每对顶点最多通过一条边连接，并且不存在与自身相连的顶点。

返回图中 最短 环的长度。如果不存在环，则返回 -1 。

环 是指以同一节点开始和结束，并且路径中的每条边仅使用一次。

 

示例 1：


输入：n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
输出：3
解释：长度最小的循环是：0 -> 1 -> 2 -> 0 
示例 2：


输入：n = 4, edges = [[0,1],[0,2]]
输出：-1
解释：图中不存在循环
 

提示：

2 <= n <= 1000
1 <= edges.length <= 1000
edges[i].length == 2
0 <= ui, vi < n
ui != vi
不存在重复的边 """

from typing import List


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        minDist = n + 1
        for i in range(n):
            q = deque([(i, -1, 0)])
            visited = [False] * n

            while q:
                node, parent, distance = q.popleft()
                if visited[node]:
                    minDist = min(minDist, distance + 1)
                    continue
                visited[node] = True

                for neighbor in graph[node]:
                    if neighbor == parent:
                        continue
                    q.append((neighbor, node, distance + 1))

        if minDist == n + 1:
            return -1
        return minDist


print(Solution().findShortestCycle(
    7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]))
# print(Solution().findShortestCycle(4, [[0, 1], [0, 2]]))
