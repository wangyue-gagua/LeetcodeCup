""" 给你数字字符串 s ，请你返回 s 中长度为 5 的 回文子序列 数目。由于答案可能很大，请你将答案对 109 + 7 取余 后返回。

提示：

如果一个字符串从前往后和从后往前读相同，那么它是 回文字符串 。
子序列是一个字符串中删除若干个字符后，不改变字符顺序，剩余字符构成的字符串。
 

示例 1：

输入：s = "103301"
输出：2
解释：
总共有 6 长度为 5 的子序列："10330" ，"10331" ，"10301" ，"10301" ，"13301" ，"03301" 。
它们中有两个（都是 "10301"）是回文的。
示例 2：

输入：s = "0000000"
输出：21
解释：所有 21 个长度为 5 的子序列都是 "00000" ，都是回文的。
示例 3：

输入：s = "9999900000"
输出：2
解释：仅有的两个回文子序列是 "99999" 和 "00000" 。
 

提示：

1 <= s.length <= 104
s 只包含数字字符。 """


from typing import Dict


class Solution:
    def countPalindromes(self, s: str) -> int:
        lens = len(s)
        if lens < 5:
            return 0
        res = 0
        # map 存储搜索过的回文子序列
        map: Dict[str, Dict[int, int]] = {}
        for left1 in range(lens - 3):
            for left2 in range(left1 + 1, lens - 2):
                joinString = s[left1] + s[left2]
                if joinString in map:
                    for right in map[joinString].keys():
                        if right > left2:
                            res += ((right - left2 - 1) * map[joinString][right]) % (10 ** 9 + 7)
                else:
                    for left3 in range(left2 + 1, lens - 1):
                        if s[left2] != s[left3]:
                            continue
                        for left4 in range(left3 + 1, lens):
                            if s[left1] == s[left4]:
                                res += (left3 - left2 - 1 ) % (10 ** 9 + 7)
                                res %= 10 ** 9 + 7
                                if joinString in map:
                                    if left3 in map[joinString]:
                                        map[joinString][left3] += 1
                                    else:
                                        map[joinString][left3] = 1
                                else:
                                    map[joinString] = {left3: 1}
        # print(map)
        return res % (10 ** 9 + 7)

print(Solution().countPalindromes("0000000"))
