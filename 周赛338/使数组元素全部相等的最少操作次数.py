""" 给你一个正整数数组 nums 。

同时给你一个长度为 m 的整数数组 queries 。第 i 个查询中，你需要将 nums 中所有元素变成 queries[i] 。你可以执行以下操作 任意 次：

将数组里一个元素 增大 或者 减小 1 。
请你返回一个长度为 m 的数组 answer ，其中 answer[i]是将 nums 中所有元素变成 queries[i] 的 最少 操作次数。

注意，每次查询后，数组变回最开始的值。

 

示例 1：

输入：nums = [3,1,6,8], queries = [1,5]
输出：[14,10]
解释：第一个查询，我们可以执行以下操作：
- 将 nums[0] 减小 2 次，nums = [1,1,6,8] 。
- 将 nums[2] 减小 5 次，nums = [1,1,1,8] 。
- 将 nums[3] 减小 7 次，nums = [1,1,1,1] 。
第一个查询的总操作次数为 2 + 5 + 7 = 14 。
第二个查询，我们可以执行以下操作：
- 将 nums[0] 增大 2 次，nums = [5,1,6,8] 。
- 将 nums[1] 增大 4 次，nums = [5,5,6,8] 。
- 将 nums[2] 减小 1 次，nums = [5,5,5,8] 。
- 将 nums[3] 减小 3 次，nums = [5,5,5,5] 。
第二个查询的总操作次数为 2 + 4 + 1 + 3 = 10 。
示例 2：

输入：nums = [2,9,6,3], queries = [10]
输出：[20]
解释：我们可以将数组中所有元素都增大到 10 ，总操作次数为 8 + 1 + 4 + 7 = 20 。 


n == nums.length
m == queries.length
1 <= n, m <= 105
1 <= nums[i], queries[i] <= 109
"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # dict存储nums中每个元素出现的次数
        numsCnt = {}
        for i in nums:
            if i in numsCnt:
                numsCnt[i] += 1
            else:
                numsCnt[i] = 1

        def oneArrMinOp(target: int):
            """数组中所有元素变为target的最少操作次数"""
            res = 0
            for i in numsCnt:
                if i < target:
                    res += (target - i) * numsCnt[i]
                elif i > target:
                    res += (i - target) * numsCnt[i]
            return res

        ans = []
        for i in queries:
            ans.append(oneArrMinOp(i))

        return ans


def minOperations(nums, queries):
    # 统计每个数出现的次数
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    sortedKeys = sorted(freq.keys())
    prefixSum = [0] * (len(sortedKeys) + 1)
    prefixCnt = [0] * (len(sortedKeys) + 1)
    prefixSum[1] = freq[sortedKeys[0]] * sortedKeys[0]
    prefixCnt[1] = freq[sortedKeys[0]]
    for i in range(2, len(prefixSum)):
        prefixSum[i] = prefixSum[
            i - 1] + freq[sortedKeys[i - 1]] * sortedKeys[i - 1]
        prefixCnt[i] = prefixCnt[i - 1] + freq[sortedKeys[i - 1]]

    def getTargetIndex(target):
        """二分查找第一个大于等于target的数在sortedKeys的下标"""
        left, right = 0, len(sortedKeys) - 1
        while left < right:
            mid = (left + right) // 2
            if sortedKeys[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    res = []
    for query in queries:
        targetIndex = getTargetIndex(query)
        if sortedKeys[targetIndex] < query:
            val = query * prefixCnt[-1] - prefixSum[-1]
        else:
            val = query * (2 * prefixCnt[targetIndex] - prefixCnt[-1]) - (2 * prefixSum[targetIndex] - prefixSum[-1])
        res.append(val)

    return res


# print(Solution().minOperations([3,1,6,8], [1,5]))
# print(Solution().minOperations([2,9,6,3], [10]))

print(minOperations([3, 1, 6, 8], [1, 5]))
print(minOperations([2, 9, 6, 3], [10]))
