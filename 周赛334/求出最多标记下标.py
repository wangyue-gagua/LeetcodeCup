""" 给你一个下标从 0 开始的整数数组 nums 。

一开始，所有下标都没有被标记。你可以执行以下操作任意次：

选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。

 

示例 1：

输入：nums = [3,5,2,4]
输出：2
解释：第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。
没有其他更多可执行的操作，所以答案为 2 。
示例 2：

输入：nums = [9,2,5,4]
输出：4
解释：第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。
第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。
没有其他更多可执行的操作，所以答案为 4 。
示例 3：

输入：nums = [7,6,8]
输出：0
解释：没有任何可以执行的操作，所以答案为 0 。 """

from typing import List, Dict


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        marked = [False] * n
        count = 0
        
        # 对于每个值num，二分搜索找到第一个 >= 2 * num的值的下标
        twoFoldIndex: Dict[int, int] = {}

        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        for i in range(n):
            if nums[i] not in twoFoldIndex:
                index = binary_search(nums, 2 * nums[i])
                # 判断是否找到了
                if index < n and nums[index] >= 2 * nums[i]:
                    twoFoldIndex[i] = index
                else:
                    twoFoldIndex[i] = -1

        # 倒序查找，如果twoFoldIndex中存在，则标记
        print(nums)
        print(twoFoldIndex)
        for i in range(n - 1, -1, -1):
            if twoFoldIndex[i] != -1:
                initIndex = twoFoldIndex[i]
                while initIndex < n and marked[initIndex]:
                    initIndex += 1
                if initIndex < n:
                    marked[initIndex] = True
                    marked[i] = True
                    count += 2

        return count


def max_num_of_indices(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    marked = [False] * n
    count = 0
    
    # 对于每个值num，二分搜索找到第一个 >= 2 * num的值的下标
    twoFoldIndex: Dict[int, int] = {}

    def binary_search(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    for i in range(n):
        if nums[i] not in twoFoldIndex:
            index = binary_search(nums, 2 * nums[i])
            # 判断是否找到了
            if index < n and nums[index] >= 2 * nums[i]:
                twoFoldIndex[i] = index
            else:
                twoFoldIndex[i] = -1

    # 倒序查找，如果twoFoldIndex中存在，则标记
    # print(nums)
    # print(twoFoldIndex)
    for i in range(n - 1, -1, -1):
        if twoFoldIndex[i] != -1:
            initIndex = twoFoldIndex[i]
            while initIndex < n and marked[initIndex]:
                initIndex += 1
            if initIndex < n:
                marked[initIndex] = True
                count += 2

    return count



# print(max_num_of_indices([3, 5, 2, 4]))
# print(max_num_of_indices([9, 2, 5, 4]))
# print(max_num_of_indices([7, 6, 8]))
# print(Solution().maxNumOfMarkedIndices([3, 5, 2, 4]))

print(Solution().maxNumOfMarkedIndices([42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]))