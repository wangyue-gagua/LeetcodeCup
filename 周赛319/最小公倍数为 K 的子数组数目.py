""" 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的 子数组 中满足 元素最小公倍数为 k 的子数组数目。

子数组 是数组中一个连续非空的元素序列。

数组的最小公倍数 是可被所有数组元素整除的最小正整数。

 

示例 1 ：

输入：nums = [3,6,2,7,1], k = 6
输出：4
解释：以 6 为最小公倍数的子数组是：
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
示例 2 ：

输入：nums = [3], k = 2
输出：0
解释：不存在以 2 为最小公倍数的子数组。 """

import math
from typing import List


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        # dp[i]表示k是否都能整除以当前元素为起始元素的连续子数组的元素

        dp = [0] * len(nums)
        res = 0

        for i in range(len(nums)):
            dp[i] = nums[i]
            if nums[i] == k:
                res += 1
            for j in range(i + 1, len(nums)):
                if k % dp[j -1] == 0:
                    dp[j] = math.lcm(dp[j - 1], nums[j])
                    if dp[j] == k:
                        res += 1
                else:
                    break
        return res

print(Solution().subarrayLCM([3], 2))

