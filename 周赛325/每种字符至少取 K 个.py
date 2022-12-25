""" 给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。

你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。

 

示例 1：

输入：s = "aabaaaacaabc", k = 2
输出：8
解释：
从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
共需要 3 + 5 = 8 分钟。
可以证明需要的最少分钟数是 8 。
示例 2：

输入：s = "a", k = 1
输出：-1
解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。 """


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # 统计每个位置的前缀和以及后缀和
        # prefix[i] = [a, b, c] 表示 s[:i] 中 a, b, c 的个数
        prefix = [[0, 0, 0]]
        for i in range(len(s)):
            prefix.append(prefix[-1][:])
            prefix[-1][ord(s[i]) - ord('a')] += 1
        suffix = []
        for prefix_i in prefix:
            suffix_i = [
                prefix[-1][0] - prefix_i[0], prefix[-1][1] - prefix_i[1],
                prefix[-1][2] - prefix_i[2]
            ]
            suffix.append(suffix_i)

        # print(prefix)
        # print(suffix)
        if prefix[-1][0] < k or prefix[-1][1] < k or prefix[-1][2] < k:
            return -1
        res = len(s)
        for i in range(len(s) + 1):
            # 从左边取 i 个字符
            # 计算剩余的字符中 a, b, c 的个数
            remain = [k - prefix[i][0], k - prefix[i][1], k - prefix[i][2]]
            # 从右边取 j 个字符
            for j in range(len(s), i, -1):
                # 计算剩余的字符中 a, b, c 的个数
                # 后缀和 = 总和 - 前缀和
                if remain[0] <= suffix[j][0] and remain[1] <= suffix[j][
                        1] and remain[2] <= suffix[j][2]:
                    res = min(res, i + len(s) - j)
                    # print(i, j, res)
                    break

        return res


# print(Solution().takeCharacters("aabaaaacaabc", 2))
# print(Solution().takeCharacters("a", 1))
print(Solution().takeCharacters("abc", 1))
