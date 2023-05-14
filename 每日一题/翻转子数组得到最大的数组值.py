""" 给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 |nums[i]-nums[i+1]| 的和。

你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。

请你找到可行的最大 数组值 。

 

示例 1：

输入：nums = [2,3,1,5,4]
输出：10
解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。
示例 2：

输入：nums = [2,4,9,24,2,1,10]
输出：68
 

提示：

1 <= nums.length <= 3*10^4
-10^5 <= nums[i] <= 10^5 """

from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        # 翻转子数组并不会改变内部的value，只会改变两个端点的value
        # 由于只能翻转一次，所以只能翻转两个端点，且只能翻转一次
        # 假设翻转的两个端点为L,R，那么翻转后的数组值为
        # 假设整个数组的value为S，那么翻转后的数组值为
        # S + abs(nums[L - 1] - nums[R])  + abs(nums[L] - nums[R + 1]) - abs(nums[L - 1] - nums[L]) - abs(nums[R] - nums[R + 1])
        # 由于翻转后的数组值只与L,R有关，所以可以枚举L,R，找到最大的数组值

        allValue = 0
        for i in range(len(nums) - 1):
            allValue += abs(nums[i] - nums[i + 1])

        ans = 0
        for L in range(len(nums) - 1):
            for R in range(L + 1, len(nums)):
                # 考虑L为0，R为len(nums) - 1的情况
                if L == 0:
                    if R == len(nums) - 1:
                        continue
                    else:
                        ans = max(ans, allValue + abs(nums[L] - nums[R + 1]) - abs(nums[R] - nums[R + 1]))
                else:
                    if R == len(nums) - 1:
                        ans = max(ans, allValue + abs(nums[L - 1] - nums[R]) - abs(nums[L - 1] - nums[L]))
                    else:
                        ans = max(ans, allValue + abs(nums[L - 1] - nums[R]) + abs(nums[L] - nums[R + 1]) - abs(
                            nums[L - 1] - nums[L]) - abs(nums[R] - nums[R + 1]))
        return ans
    
print(Solution().maxValueAfterReverse([2,3,1,5,4]))
print(Solution().maxValueAfterReverse([2,4,9,24,2,1,10]))
print(Solution().maxValueAfterReverse([2,5,1,3,4]))