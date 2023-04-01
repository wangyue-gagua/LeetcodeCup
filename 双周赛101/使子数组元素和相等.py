""" 给你一个下标从 0 开始的整数数组 arr 和一个整数 k 。数组 arr 是一个循环数组。换句话说，数组中的最后一个元素的下一个元素是数组中的第一个元素，数组中第一个元素的前一个元素是数组中的最后一个元素。

你可以执行下述运算任意次：

选中 arr 中任意一个元素，并使其值加上 1 或减去 1 。
执行运算使每个长度为 k 的 子数组 的元素总和都相等，返回所需要的最少运算次数。

子数组 是数组的一个连续部分。

 

示例 1：

输入：arr = [1,4,1,3], k = 2
输出：1
解释：在下标为 1 的元素那里执行一次运算，使其等于 3 。
执行运算后，数组变为 [1,3,1,3] 。
- 0 处起始的子数组为 [1, 3] ，元素总和为 4 
- 1 处起始的子数组为 [3, 1] ，元素总和为 4 
- 2 处起始的子数组为 [1, 3] ，元素总和为 4 
- 3 处起始的子数组为 [3, 1] ，元素总和为 4 
示例 2：

输入：arr = [2,5,5,7], k = 3
输出：5
解释：在下标为 0 的元素那里执行三次运算，使其等于 5 。在下标为 3 的元素那里执行两次运算，使其等于 5 。
执行运算后，数组变为 [5,5,5,5] 。
- 0 处起始的子数组为 [5, 5, 5] ，元素总和为 15
- 1 处起始的子数组为 [5, 5, 5] ，元素总和为 15
- 2 处起始的子数组为 [5, 5, 5] ，元素总和为 15
- 3 处起始的子数组为 [5, 5, 5] ，元素总和为 15
 

提示：

1 <= k <= arr.length <= 105
1 <= arr[i] <= 109 """

from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        # 已知为循环数组，故对于每个长度为k的子数组
        # 对于所有i，有 a[i] = a[(i + k) % len(arr)]
        # 将所有相等的a[i]放入一个集合内
        res = 0

        def selectPos(arr: List[int]):
            # 选择一个位置，使得该位置的值与其他位置的值的差的绝对值之和最小
            # 选择中位数
            arr.sort()
            return arr[len(arr) // 2]

        allReadyUsed = set()
        for i in range(k):
            if i in allReadyUsed:
                continue
            sameSet = set()
            sameSet.add(i)
            allReadyUsed.add(i)
            j = i
            while True:
                nextIndex = (j + k) % len(arr)
                if nextIndex in sameSet:
                    break
                sameSet.add(nextIndex)
                allReadyUsed.add(nextIndex)
                j = nextIndex
            arrVal = [arr[i] for i in sameSet]
            sameArrVal = selectPos(arrVal)

            for i in sameSet:
                res += abs(arr[i] - sameArrVal)
        return res


print(Solution().makeSubKSumEqual([1, 4, 1, 3], 2))
print(Solution().makeSubKSumEqual([2, 5, 5, 7], 3))
print(Solution().makeSubKSumEqual([2, 10, 9], 1))