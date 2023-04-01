""" 给你两个只包含 1 到 9 之间数字的数组 nums1 和 nums2 ，每个数组中的元素 互不相同 ，请你返回 最小 的数字，两个数组都 至少 包含这个数字的某个数位。
 

示例 1：

输入：nums1 = [4,1,3], nums2 = [5,7]
输出：15
解释：数字 15 的数位 1 在 nums1 中出现，数位 5 在 nums2 中出现。15 是我们能得到的最小数字。
示例 2：

输入：nums1 = [3,5,2,6], nums2 = [3,1,7]
输出：3
解释：数字 3 的数位 3 在两个数组中都出现了。 
1 <= nums1.length, nums2.length <= 9
1 <= nums1[i], nums2[i] <= 9
"""

from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        # 如果存在相同的数字，则返回相同的数字中最小的
        if set(nums1) & set(nums2):
            return min(set(nums1) & set(nums2))
        # 如果不存在相同的数字，则返回两个数组中最小的数字的组合
        min1 = min(nums1)
        min2 = min(nums2)
        return min1 * 10 + min2 if min1 < min2 else min2 * 10 + min1
    
print(Solution().minNumber([4,1,3], [5,7]))
print(Solution().minNumber([3,5,2,6], [3,1,7]))