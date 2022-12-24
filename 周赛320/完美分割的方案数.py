""" 给你一个字符串 s ，每个字符是数字 '1' 到 '9' ，再给你两个整数 k 和 minLength 。

如果对 s 的分割满足以下条件，那么我们认为它是一个 完美 分割：

s 被分成 k 段互不相交的子字符串。
每个子字符串长度都 至少 为 minLength 。
每个子字符串的第一个字符都是一个 质数 数字，最后一个字符都是一个 非质数 数字。质数数字为 '2' ，'3' ，'5' 和 '7' ，剩下的都是非质数数字。
请你返回 s 的 完美 分割数目。由于答案可能很大，请返回答案对 109 + 7 取余 后的结果。

一个 子字符串 是字符串中一段连续字符串序列。

 

示例 1：

输入：s = "23542185131", k = 3, minLength = 2
输出：3
解释：存在 3 种完美分割方案：
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"
示例 2：

输入：s = "23542185131", k = 3, minLength = 3
输出：1
解释：存在一种完美分割方案："2354 | 218 | 5131" 。
示例 3：

输入：s = "3312958", k = 3, minLength = 1
输出：1
解释：存在一种完美分割方案："331 | 29 | 58" 。
 

提示：

1 <= k, minLength <= s.length <= 1000
s 每个字符都为数字 '1' 到 '9' 之一。 """

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        def isPrime(n):
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5)+1, 2):
                if n % i == 0:
                    return False
            return True

        n = len(s)
        dp = [[0] * (n+1) for _ in range(k+1)]
        dp[0][0] = 1
        for i in range(1, k+1):
            for j in range(i*minLength, n+1):
                for l in range(minLength, j+1):
                    if isPrime(int(s[j-l])) and not isPrime(int(s[j-1])):
                        dp[i][j] += dp[i-1][j-l]
                        dp[i][j] %= 10**9 + 7
        
        print(dp)
        return dp[k][n]

print(Solution().beautifulPartitions("3312958", 3, 1))