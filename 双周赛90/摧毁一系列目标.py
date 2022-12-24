"""
给你一个下标从 0 开始的数组 nums ，它包含若干正整数，表示数轴上你需要摧毁的目标所在的位置。同时给你一个整数 space 。

你有一台机器可以摧毁目标。给机器 输入 nums[i] ，这台机器会摧毁所有位置在 nums[i] + c * space 的目标，其中 c 是任意非负整数。你想摧毁 nums 中 尽可能多 的目标。

请你返回在摧毁数目最多的前提下，nums[i] 的 最小值 。

 

示例 1：

输入：nums = [3,7,8,1,1,5], space = 2
输出：1
解释：如果我们输入 nums[3] ，我们可以摧毁位于 1,3,5,7,9,... 这些位置的目标。
这种情况下， 我们总共可以摧毁 5 个目标（除了 nums[2]）。
没有办法摧毁多于 5 个目标，所以我们返回 nums[3] 。
示例 2：

输入：nums = [1,3,5,2,4,6], space = 2
输出：1
解释：输入 nums[0] 或者 nums[3] 都会摧毁 3 个目标。
没有办法摧毁多于 3 个目标。
由于 nums[0] 是最小的可以摧毁 3 个目标的整数，所以我们返回 1 。
示例 3：

输入：nums = [6,2,5], space = 100
输出：2
解释：无论我们输入哪个数字，都只能摧毁 1 个目标。输入的最小整数是 nums[1] 。
"""

from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        """此方法超时 41 / 44 个通过测试用例"""
        n = len(nums)
        nums.sort()
        searchedIndex = set()
        minNum = 10**9
        minNumCount = 0
        for i in range(n):
            if i in searchedIndex:
                continue
            # if n - i <= minNumCount:
            #     break
            searchedIndex.add(i)
            count = 1
            for j in range(i + 1, n):
                if j in searchedIndex:
                    continue
                if (nums[j] - nums[i]) % space == 0:
                    count += 1
                    searchedIndex.add(j)
            if count > minNumCount:
                minNum = nums[i]
                minNumCount = count
        return minNum

print(Solution().destroyTargets([1,3,5,2,4,6], 2))
