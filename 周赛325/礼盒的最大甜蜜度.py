""" 给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。

商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。

返回礼盒的 最大 甜蜜度。

 

示例 1：

输入：price = [13,5,1,8,21,2], k = 3
输出：8
解释：选出价格分别为 [13,5,21] 的三类糖果。
礼盒的甜蜜度为 min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8 。
可以证明能够取得的最大甜蜜度就是 8 。
示例 2：

输入：price = [1,3,1], k = 2
输出：2
解释：选出价格分别为 [1,3] 的两类糖果。 
礼盒的甜蜜度为 min(|1 - 3|) = min(2) = 2 。
可以证明能够取得的最大甜蜜度就是 2 。
示例 3：

输入：price = [7,7,7,7], k = 2
输出：0
解释：从现有的糖果中任选两类糖果，甜蜜度都会是 0 。 """

import bisect
from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        print(price)
        # 将最大值到最小值的区间获取k个点
        if k == 2:
            return price[-1] - price[0]
        else:
            interval = (price[-1] - price[0]) / (k - 1)
            # 从最小值开始，每隔interval取一个点
            # 寻找数组中最接近该点的值，并计算与上一个点的差值
            last = price[0]
            res = price[-1] - price[0]
            for _ in range(1, k - 1):
                index = bisect.bisect_left(price, last + interval)
                if index == 1:
                    res = min(res, price[index] - last)
                else:
                    if price[index] - (last + interval) > (
                            last + interval) - price[index - 1]:
                        index -= 1
                    print(res, index, last)
                    res = min(res, price[index] - last, price[-1] - price[index])
                last = price[index]
            return res


# print(Solution().maximumTastiness([13, 5, 1, 8, 21, 2], 3))
# print(Solution().maximumTastiness([1,3,1], 2))
# print(Solution().maximumTastiness([7,7,7,7], 2))
print(Solution().maximumTastiness([34,116,83,15,150,56,69,42,26], 6))