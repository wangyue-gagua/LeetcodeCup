""" You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

 

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14 """

from math import gcd
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        dp = [[0] * (1 << (2 * n)) for _ in range(n + 1)]
        print(dp)
        for i in range(1, n + 1):
            for mask in range(1 << (2 * n)):
                if bin(mask).count('1') == 2 * i:
                    for j in range(2 * n):
                        if mask & (1 << j):
                            for k in range(j + 1, 2 * n):
                                if mask & (1 << k):
                                    dp[i][mask] = max(dp[i][mask], dp[i - 1][mask ^ (1 << j) ^ (1 << k)] + i * gcd(nums[j], nums[k]))
        return dp[n][(1 << (2 * n)) - 1]

print(Solution().maxScore([3,4,6,8]))