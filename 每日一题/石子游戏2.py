""" 爱丽丝和鲍勃继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。

爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初，M = 1。

在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。

游戏一直持续到所有石子都被拿走。

假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。

 

示例 1：

输入：piles = [2,7,9,4,4]
输出：10
解释：如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 = 10堆。如果Alice一开始拿走了两堆，那么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。
示例 2:

输入：piles = [1,2,3,4,5,100]
输出：104
 

提示：

1 <= piles.length <= 100
1 <= piles[i] <= 104 """

from math import inf, floor
from typing import List
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # 记忆化搜索

        prefixSum = [0]
        for p in piles:
            prefixSum.append(prefixSum[-1] + p)

        @lru_cache(None)
        def dfs(i, m):
            """
            博弈问题。令 dfs(i,m)\textit{dfs}(i, m)dfs(i,m) 表示前 iii 堆石头已经被取走，
            当前的 M=mM = mM=m 的情况下，接下去取石头的玩家可以比另一方多取的石头数"""
            if i == len(piles):
                return 0

            res = -inf
            for x in range(1, 2 * m + 1):
                if i + x > len(piles):
                    break
                res = max(
                    res,
                    prefixSum[i + x] - prefixSum[i] - dfs(i + x, max(m, x)))

            return res

        ret = floor((prefixSum[-1] + dfs(0, 1)) / 2)
        return ret


print(Solution().stoneGameII([2, 7, 9, 4, 4]))
print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]))
