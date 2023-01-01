"""
给你两个正整数 left 和 right ，请你找到两个整数 num1 和 num2 ，它们满足：

left <= nums1 < nums2 <= right  。
nums1 和 nums2 都是 质数 。
nums2 - nums1 是满足上述条件的质数对中的 最小值 。
请你返回正整数数组 ans = [nums1, nums2] 。如果有多个整数对满足上述条件，请你返回 nums1 最小的质数对。如果不存在符合题意的质数对，请你返回 [-1, -1] 。

如果一个整数大于 1 ，且只能被 1 和它自己整除，那么它是一个质数。

示例 1：

输入：left = 10, right = 19
输出：[11,13]
解释：10 到 19 之间的质数为 11 ，13 ，17 和 19 。
质数对的最小差值是 2 ，[11,13] 和 [17,19] 都可以得到最小差值。
由于 11 比 17 小，我们返回第一个质数对。
示例 2：

输入：left = 4, right = 6
输出：[-1,-1]
解释：给定范围内只有一个质数，所以题目条件无法被满足。
"""

from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # 生成素数表 10^6

        def getPrimeList(left, right):
            # 埃托拉斯特尼筛法求范围内的素数
            primeList = []
            isPrime = [True] * (right + 1)
            for i in range(2, right + 1):
                if isPrime[i]:
                    if left <= i:
                        primeList.append(i)
                    for j in range(i * i, right + 1, i):
                        isPrime[j] = False
            return primeList

        primeList = getPrimeList(left, right)
        if len(primeList) < 2:
            return [-1, -1]
        minLeft = primeList[0]
        minRight = primeList[-1]
        for i in range(len(primeList) - 1):
            diff = primeList[i + 1] - primeList[i]
            # if diff == 2:
            #     return [primeList[i], primeList[i + 1]]
            if diff < minRight - minLeft:
                minLeft = primeList[i]
                minRight = primeList[i + 1]
        return [minLeft, minRight]


print(Solution().closestPrimes(431823, 921113))
print(Solution().closestPrimes(341663, 815604))