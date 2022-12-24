""" 给你一个 n 个点的无向图，节点从 0 到 n - 1 编号。给你一个长度为 n 下标从 0 开始的整数数组 vals ，其中 vals[i] 表示第 i 个节点的值。

同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条双向边。

星图 是给定图中的一个子图，它包含一个中心节点和 0 个或更多个邻居。换言之，星图是给定图中一个边的子集，且这些边都有一个公共节点。

下图分别展示了有 3 个和 4 个邻居的星图，蓝色节点为中心节点。



星和 定义为星图中所有节点值的和。

给你一个整数 k ，请你返回 至多 包含 k 条边的星图中的 最大星和 。

 

示例 1：



输入：vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2
输出：16
解释：上图展示了输入示例。
最大星和对应的星图在上图中用蓝色标出。中心节点是 3 ，星图中还包含邻居 1 和 4 。
无法得到一个和大于 16 且边数不超过 2 的星图。
示例 2：

输入：vals = [-5], edges = [], k = 0
输出：-5
解释：只有一个星图，就是节点 0 自己。
所以我们返回 -5 。
 

提示：

n == vals.length
1 <= n <= 105
-104 <= vals[i] <= 104
0 <= edges.length <= min(n * (n - 1) / 2, 105)
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
0 <= k <= n - 1 """

from typing import List
import heapq


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # 初始化一个大小为k的最大堆
        # neighbors[i] = heapq.heapify([0] * k)
        # 遍历edges，将每个节点的邻居节点的值加入到neighbors[i]中
        neighbors = [[0] * k for _ in range(len(vals))]
        for neighbor in neighbors:
            heapq.heapify(neighbor)
        # print(neighbors)
        for edge in edges:
            heapq.heappush(neighbors[edge[0]], vals[edge[1]])
            heapq.heappush(neighbors[edge[1]], vals[edge[0]])
        # print(heapq.nlargest(2, neighbors[0]))
        
        maxStarSum = -10 ** 4
        for i in range(len(vals)):
            maxStarSum = max(maxStarSum, vals[i] + sum(heapq.nlargest(k, neighbors[i])))
        return maxStarSum



        

        



print(Solution().maxStarSum(vals = [-5], edges = [], k = 0))
print(Solution().maxStarSum(vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2))
    
