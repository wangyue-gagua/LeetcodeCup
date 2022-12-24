"""
给你一个长度为 n 的 整数 数组 pref 。找出并返回满足下述条件且长度为 n 的数组 arr ：

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
注意 ^ 表示 按位异或（bitwise-xor）运算。

可以证明答案是 唯一 的。
"""

from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [0] * len(pref)
        res[0] = pref[0]
        # for i in range(1, len(pref)):
        #     temp = 0
        #     for j in range(i):
        #         temp ^= res[j]
        #     res[i] = temp ^ pref[i]
        # return res

        # 记忆化
        xorList = [0] * len(pref)
        xorList[0] = pref[0]
        for i in range(1, len(pref)):
            res[i] = xorList[i - 1] ^ pref[i]
            xorList[i] = xorList[i - 1] ^ res[i]
        return res

    

print(Solution().findArray([13]))