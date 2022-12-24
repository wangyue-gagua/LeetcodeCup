"""
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。
"""

from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[30001 for _ in range(n)] for _ in range(n)]
        dp[0][0] = arr[0]
        # print(dp)
        for i in range(1, n):
            for j in range(i + 1):
                if dp[i - 1][j] < arr[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = arr[i]
        res = 0
        # print(dp)
        for i in range(n):
            for j in range(i + 1):
                res += dp[i][j]
        return res % (10 ** 9 + 7)

        # # 单调栈
        # stack = []
        # res = 0
        # dp = [0 for _ in range(n)]
        # for i, x in enumerate(arr):
        #     while stack and arr[stack[-1]] > x:
        #         stack.pop()
        #     k = i - stack[-1] if stack else i + 1
        #     dp[i] = dp[i - k] + k * x if stack else k * x
        #     res = (res + dp[i]) % (10 ** 9 + 7)
        #     stack.append(i)
        # return res

# print(Solution().sumSubarrayMins([3, 1, 2, 4]))
