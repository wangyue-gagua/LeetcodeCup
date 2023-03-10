""" 给你一个下标从 0 开始的字符串 word ，长度为 n ，由从 0 到 9 的数字组成。另给你一个正整数 m 。

word 的 可整除数组 div  是一个长度为 n 的整数数组，并满足：

如果 word[0,...,i] 所表示的 数值 能被 m 整除，div[i] = 1
否则，div[i] = 0
返回 word 的可整除数组。

 

示例 1：

输入：word = "998244353", m = 3
输出：[1,1,0,0,0,1,1,0,0]
解释：仅有 4 个前缀可以被 3 整除："9"、"99"、"998244" 和 "9982443" 。
示例 2：

输入：word = "1010", m = 10
输出：[0,1,0,1]
解释：仅有 2 个前缀可以被 10 整除："10" 和 "1010" 。
 

提示：

1 <= n <= 105
word.length == n
word 由数字 0 到 9 组成
1 <= m <= 109 """

from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = [0] * len(word)
        cur = 0
        for i in range(len(word)):
            curCharInt = int(word[i])
            if cur % m == 0:
                if curCharInt % m == 0:
                    res[i] = 1
                    cur = 0
                else:
                    cur = curCharInt
            else:
                cur = cur * 10 + curCharInt
                if cur % m == 0:
                    res[i] = 1
                    cur = 0
                else:
                    continue

        return res


# print(Solution().divisibilityArray("998244353", 3))

# print(Solution().divisibilityArray("100", 10))


def find_divisible_array(word: str, m: int) -> List[int]:
    n = len(word)
    mod = [0] * n
    mod[0] = int(word[0]) % m
    for i in range(1, n):
        mod[i] = (mod[i - 1] * 10 + int(word[i])) % m
    divisible = [0] * n
    for i in range(n):
        if mod[i] == 0:
            divisible[i] = 1
    return divisible


print(find_divisible_array("998244353", 3))
print(find_divisible_array("100", 10))
