"""
给你两个下标从 0 开始的数组 nums 和 cost ，分别包含 n 个 正 整数。

你可以执行下面操作 任意 次：

将 nums 中 任意 元素增加或者减小 1 。
对第 i 个元素执行一次操作的开销是 cost[i] 。

请你返回使 nums 中所有元素 相等 的 最少 总开销。

 输入：nums = [1,3,5,2], cost = [2,3,1,14]
输出：8
解释：我们可以执行以下操作使所有元素变为 2 ：
- 增加第 0 个元素 1 次，开销为 2 。
- 减小第 1 个元素 1 次，开销为 3 。
- 减小第 2 个元素 3 次，开销为 1 + 1 + 1 = 3 。
总开销为 2 + 3 + 3 = 8 。
这是最小开销。
"""
from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # 线性规划问题
        numCost = []
        for i in range(len(nums)):
            numCost.append([nums[i], cost[i]])

        numCost.sort(key=lambda x: x[1], reverse=True)
        def calCost(num):
            return sum([abs(num - i[0]) * i[1] for i in numCost])

        minCost = calCost(numCost[0][0])
        for i in range(1, len(numCost)):
            if numCost[i][0] == numCost[i - 1][0]:
                continue
            minCost = min(minCost, calCost(numCost[i][0]))
        return minCost

print(Solution().minCost([1,3,5,2], [2,3,1,14]))



