""" 给你一个下标从 0 开始的整数数组 nums ，数组长度为 n 。

你可以执行无限次下述运算：

选择一个之前未选过的下标 i ，并选择一个 严格小于 nums[i] 的质数 p ，从 nums[i] 中减去 p 。
如果你能通过上述运算使得 nums 成为严格递增数组，则返回 true ；否则返回 false 。

严格递增数组 中的每个元素都严格大于其前面的元素。

 

示例 1：

输入：nums = [4,9,6,10]
输出：true
解释：
在第一次运算中：选择 i = 0 和 p = 3 ，然后从 nums[0] 减去 3 ，nums 变为 [1,9,6,10] 。
在第二次运算中：选择 i = 1 和 p = 7 ，然后从 nums[1] 减去 7 ，nums 变为 [1,2,6,10] 。
第二次运算后，nums 按严格递增顺序排序，因此答案为 true 。
示例 2：

输入：nums = [6,8,11,12]
输出：true
解释：nums 从一开始就按严格递增顺序排序，因此不需要执行任何运算。
示例 3：

输入：nums = [5,8,3]
输出：false
解释：可以证明，执行运算无法使 nums 按严格递增顺序排序，因此答案是 false 。

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
nums.length == n
  """

from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # 质数需要严格小于nums[i]，故最后得到的num[i] >= 1
        # 且nums[i] - p >= 1，故p <= nums[i] - 1

        # 生成从2到1000的质数列表
        prime_list = [2]
        for i in range(3, 1001):
            for j in prime_list:
                if i % j == 0:
                    break
            else:
                prime_list.append(i)

        # 从前往后遍历nums，倒序质数表暴力查找最大的小于nums[i]的质数p，且需要满足nums[i] - p > nums[i - 1]
        # 如果没有p能满足这个条件，返回False

        # 处理nums[0]
        for i in prime_list[::-1]:
            if i < nums[0]:
                nums[0] -= i
                break

        # 处理nums[1:]
        for i in range(1, len(nums)):
            for j in prime_list[::-1]:
                if j < nums[i] and nums[i] - j > nums[i - 1]:
                    nums[i] -= j
                    break
            else:
                if nums[i] <= nums[i - 1]:
                    return False
            
        return True


print(Solution().primeSubOperation([4, 9, 6, 10]))
print(Solution().primeSubOperation([6, 8, 11, 12]))
print(Solution().primeSubOperation([5, 8, 3]))
print(Solution().primeSubOperation([998, 2]))
