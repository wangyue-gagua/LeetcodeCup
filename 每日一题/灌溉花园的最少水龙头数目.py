""" 在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。

花园里总共有 n + 1 个水龙头，分别位于 [0, 1, ..., n] 。

给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）表示：如果打开点 i 处的水龙头，可以灌溉的区域为 [i -  ranges[i], i + ranges[i]] 。

请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 -1 。

 

示例 1：



输入：n = 5, ranges = [3,4,1,1,0,0]
输出：1
解释：
点 0 处的水龙头可以灌溉区间 [-3,3]
点 1 处的水龙头可以灌溉区间 [-3,5]
点 2 处的水龙头可以灌溉区间 [1,3]
点 3 处的水龙头可以灌溉区间 [2,4]
点 4 处的水龙头可以灌溉区间 [4,4]
点 5 处的水龙头可以灌溉区间 [5,5]
只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。
示例 2：

输入：n = 3, ranges = [0,0,0,0]
输出：-1
解释：即使打开所有水龙头，你也无法灌溉整个花园。 """

from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """贪心算法 o(n^2)"""
        def resolve1():
            # 1. 将每个水龙头的左右边界放入一个数组中
            # 2. 对数组进行排序, 每次取出左边界最小的区间, 将其右边界作为新的左边界, 重复上述步骤, 直到右边界大于等于n
            # 3. 如果右边界小于n, 则说明无法灌溉整个花园, 返回-1
            # 4. 否则返回步骤2中的次数

            # 1. 将每个水龙头的左右边界放入一个数组中
            intervals = []
            for i, r in enumerate(ranges):
                if r == 0:
                    continue
                intervals.append((i - r, i + r))

            # 2. 对数组进行排序, 每次取出左边界最小的区间, 将其右边界作为新的左边界, 重复上述步骤, 直到右边界大于等于n
            intervals.sort(key=lambda x: x[0])
            # print(intervals)

            left, right = 0, 0
            count = 0
            while left < n:
                # print(left, right)
                count += 1
                for l, r in intervals:
                    if l <= left:
                        right = max(right, r)
                    else:
                        break
                if right <= left:
                    return -1
                left = right
            return count

        def resolve2():
            """贪心算法 o(n)
            预处理所有的子区间，对于每一个位置 i，我们记录以其为左端点的子区间中最远的右端点，记为 rightMost[i]
            """

            rightMost = [0] * (n + 1)
            for i, r in enumerate(ranges):
                left, right = max(i - r, 0), min(i + r, n)
                rightMost[left] = max(rightMost[left], right)

            last, ret, pre = 0, 0, 0
            for i in range(n):
                last = max(last, rightMost[i])
                if i == last:
                    return -1
                if i == pre:
                    ret += 1
                    pre = last
            return ret

        return resolve2()



print(Solution().minTaps(5, [3, 4, 1, 1, 0, 0]))