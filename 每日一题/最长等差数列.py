""" 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。

回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。并且如果 seq[i+1] - seq[i]( 0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。

 

示例 1：

输入：nums = [3,6,9,12]
输出：4
解释： 
整个数组是公差为 3 的等差数列。
示例 2：

输入：nums = [9,4,7,2,10]
输出：3
解释：
最长的等差子序列是 [4,7,10]。
示例 3：

输入：nums = [20,1,15,3,10,5,8]
输出：4
解释：
最长的等差子序列是 [20,15,10,5]。
 

提示：

2 <= nums.length <= 1000
0 <= nums[i] <= 500 """

from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # 动态规划
        # dp[i][j] 表示以 nums[i] 结尾，公差为 j 的最长等差数列的长度
        # 状态转移方程为 dp[i][j] = dp[k][j] + 1 (0 <= k < i)
        # 由于公差可能为负数，所以需要将公差加上 500，使其变为正数
        # 由于公差可能为 0，所以需要将公差加上 500，使其不为 0
        # 由于公差可能为 500，所以需要将公差加上 500，使其不为 1000
        # 最后返回 dp[i][j] 中的最大值
        dp = [[0] * 1001 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                dp[i][nums[i] - nums[j] + 500] = dp[j][nums[i] - nums[j] + 500] + 1
        
        max = 0
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j] > max:
                    max = dp[i][j]
        return max + 1

    
print(Solution().longestArithSeqLength([3,6,9,12]))
print(Solution().longestArithSeqLength([9,4,7,2,10]))
print(Solution().longestArithSeqLength([20,1,15,3,10,5,8]))