# edges[i] = [ui, vi] 表示顶点 ui 和 vi 之间存在一条边
# 求最小环长度

from typing import List

from collections import deque


def shortestCycle(edges, n):
    val = [[0 for i in range(n + 1)] for j in range(n + 1)] # 原图的邻接矩阵

    def floyd(n):
        dis = [[0 for i in range(n + 1)] for j in range(n + 1)] # 最短路矩阵
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = val[i][j] # 初始化最短路矩阵
        ans = inf
        for k in range(1, n + 1):
            for i in range(1, k):
                for j in range(1, i):
                    ans = min(ans, dis[i][j] + val[i][k] + val[k][j]) # 更新答案
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]) # 正常的 floyd 更新最短路矩阵
        return ans



print(
    shortestCycle([[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]], 7))
print(shortestCycle([[0, 1], [0, 2]], 4))
