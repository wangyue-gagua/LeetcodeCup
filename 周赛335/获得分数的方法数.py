""" 考试中有 n 种类型的题目。给你一个整数 target 和一个下标从 0 开始的二维整数数组 types ，其中 types[i] = [counti, marksi] 表示第 i 种类型的题目有 counti 道，每道题目对应 marksi 分。

返回你在考试中恰好得到 target 分的方法数。由于答案可能很大，结果需要对 109 +7 取余。

注意，同类型题目无法区分。

比如说，如果有 3 道同类型题目，那么解答第 1 和第 2 道题目与解答第 1 和第 3 道题目或者第 2 和第 3 道题目是相同的。
 

示例 1：

输入：target = 6, types = [[6,1],[3,2],[2,3]]
输出：7
解释：要获得 6 分，你可以选择以下七种方法之一：
- 解决 6 道第 0 种类型的题目：1 + 1 + 1 + 1 + 1 + 1 = 6
- 解决 4 道第 0 种类型的题目和 1 道第 1 种类型的题目：1 + 1 + 1 + 1 + 2 = 6
- 解决 2 道第 0 种类型的题目和 2 道第 1 种类型的题目：1 + 1 + 2 + 2 = 6
- 解决 3 道第 0 种类型的题目和 1 道第 2 种类型的题目：1 + 1 + 1 + 3 = 6
- 解决 1 道第 0 种类型的题目、1 道第 1 种类型的题目和 1 道第 2 种类型的题目：1 + 2 + 3 = 6
- 解决 3 道第 1 种类型的题目：2 + 2 + 2 = 6
- 解决 2 道第 2 种类型的题目：3 + 3 = 6
示例 2：

输入：target = 5, types = [[50,1],[50,2],[50,5]]
输出：4
解释：要获得 5 分，你可以选择以下四种方法之一：
- 解决 5 道第 0 种类型的题目：1 + 1 + 1 + 1 + 1 = 5
- 解决 3 道第 0 种类型的题目和 1 道第 1 种类型的题目：1 + 1 + 1 + 2 = 5
- 解决 1 道第 0 种类型的题目和 2 道第 1 种类型的题目：1 + 2 + 2 = 5
- 解决 1 道第 2 种类型的题目：5
示例 3：

输入：target = 18, types = [[6,1],[3,2],[2,3]]
输出：1
解释：只有回答所有题目才能获得 18 分。
  """

from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # 二维dp
        # dp[i][j]表示前i种题目，得到j分的方法数
        # counti = types[i-1][0] marksi = types[i-1][1]
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-marksi] + dp[i-1][j-2*marksi] + ... + dp[i-1][j-counti*marksi]

        dp = [[0] * (target + 1) for _ in range(len(types) + 1)]
        dp[0][0] = 1
        for i in range(1, len(types) + 1):
            counti = types[i - 1][0]
            marksi = types[i - 1][1]
            for j in range(target + 1):
                for k in range(counti + 1):
                    if j - k * marksi >= 0:
                        dp[i][j] += dp[i - 1][j - k * marksi]
                        dp[i][j] %= (10 ** 9 + 7)
                    else:
                        break
        return dp[-1][-1] % (10 ** 9 + 7)


print(Solution().waysToReachTarget(6, [[6, 1], [3, 2], [2, 3]]))
print(Solution().waysToReachTarget(5, [[50, 1], [50, 2], [50, 5]]))
print(Solution().waysToReachTarget(18, [[6, 1], [3, 2], [2, 3]]))
