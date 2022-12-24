"""
给你两个正整数 n 和 target 。

如果某个整数每一位上的数字相加小于或等于 target ，则认为这个整数是一个 美丽整数 。

找出并返回满足 n + x 是 美丽整数 的最小非负整数 x 。生成的输入保证总可以使 n 变成一个美丽整数。

 

示例 1：

输入：n = 16, target = 6
输出：4
解释：最初，n 是 16 ，且其每一位数字的和是 1 + 6 = 7 。在加 4 之后，n 变为 20 且每一位数字的和变成 2 + 0 = 2 。可以证明无法加上一个小于 4 的非负整数使 n 变成一个美丽整数。
示例 2：

输入：n = 467, target = 6
输出：33
解释：最初，n 是 467 ，且其每一位数字的和是 4 + 6 + 7 = 17 。在加 33 之后，n 变为 500 且每一位数字的和变成 5 + 0 + 0 = 5 。可以证明无法加上一个小于 33 的非负整数使 n 变成一个美丽整数。
示例 3：

输入：n = 1, target = 1
输出：0
解释：最初，n 是 1 ，且其每一位数字的和是 1 ，已经小于等于 target 。
"""

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        """91 / 92 个通过测试用例"""
        nStr = str(n)
        nLen = len(nStr)
        if nLen == 1:
            if int(nStr) <= target:
                return 0
            else:
                return 10 - int(nStr)
        for i in range(nLen):
            if target - int(nStr[i]) > 0:
                target -= int(nStr[i])
            elif target - int(nStr[i]) == 0:
                for j in range(i + 1, nLen):
                    if int(nStr[j]) != 0:
                        return 10 ** (nLen - i) - int(nStr[i:])
                return 0
                        
            else:
                # print(n % (10 ** (nLen - i)), target, i, n)
                # return self.makeIntegerBeautiful( n % (10 ** (nLen - i)), target)
                return 10 ** (nLen - i) - int(nStr[i:])
        return 0

print(Solution().makeIntegerBeautiful(666, 100))

