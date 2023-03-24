""" 给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正整数 k 。

统计并返回 num 中的 中位数 等于 k 的非空子数组的数目。

注意：

数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位数是位于中间靠 左 的那个元素。
例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
子数组是数组中的一个连续部分。
 

示例 1：

输入：nums = [3,2,1,4,5], k = 4
输出：3
解释：中位数等于 4 的子数组有：[4]、[4,5] 和 [1,4,5] 。
示例 2：

输入：nums = [2,3,1], k = 3
输出：1
解释：[3] 是唯一一个中位数等于 3 的子数组。
 

提示：

n == nums.length
1 <= n <= 105
1 <= nums[i], k <= n
nums 中的整数互不相同
 """

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        lens = len(nums)
        # 子数组必定包含k
        indexK = nums.index(k)
        res = 1
        # dp[i][0] 表示从i到idnexK的子数组中小于k的数字的数量
        # dp[i][1] 表示从i到idnexK的子数组中大于k的数字的数量
        dp = [[0, 0] for _ in range(lens)]
        dp[indexK][0] = dp[indexK][1] = 0
        for i in range(indexK - 1, -1, -1):
            if nums[i] < k:
                dp[i][0] = dp[i + 1][0] + 1
                dp[i][1] = dp[i + 1][1]
            else:
                dp[i][0] = dp[i + 1][0]
                dp[i][1] = dp[i + 1][1] + 1
            # 处理以indexK为右端点的情况
            subLen = indexK - i
            if subLen % 2 == 0:
                # 中位数为k
                if dp[i][0] == dp[i][1]:
                    res += 1
            else:
                # 中位数不为k
                if dp[i][0] + 1 == dp[i][1]:
                    res += 1
        for i in range(indexK + 1, lens):
            if nums[i] < k:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1]
            else:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1] + 1
            # 处理以indexK为左端点的情况
            subLen = i - indexK
            if subLen % 2 == 0:
                # 中位数为k
                if dp[i][0] == dp[i][1]:
                    res += 1
            else:
                # 中位数不为k
                if dp[i][0] + 1 == dp[i][1]:
                    res += 1
        
        # 左端点为i, 右端点为j
        for i in range(indexK):
            if abs(dp[i][0] - dp[i][1]) > lens - indexK:
                continue
            for j in range(indexK + 1, lens):
                # 总数量为 j-i
                # 小于k的数量为 dp[i][0] + dp[j][0]
                # 大于k的数量为 dp[i][1] + dp[j][1]
                subLen = j - i
                if subLen % 2 == 0:
                    # 中位数为k
                    if dp[i][0] + dp[j][0] == dp[i][1] + dp[j][1]:
                        res += 1
                else:
                    # 中位数不为k
                    if dp[i][0] + dp[j][0] + 1 == dp[i][1] + dp[j][1]:
                        res += 1
            
        # print(dp)
        return res

print(Solution().countSubarrays([2,3,1], 3))
print(Solution().countSubarrays([3,2,1,4,5], 4))
print(Solution().countSubarrays([2,5,1,4,3,6], 1)) # 3
