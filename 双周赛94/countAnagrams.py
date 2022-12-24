""" You are given a string s containing one or more words. Every consecutive pair of words is separated by a single space ' '.

A string t is an anagram of string s if the ith word of t is a permutation of the ith word of s.

For example, "acb dfe" is an anagram of "abc def", but "def cab" and "adc bef" are not.
Return the number of distinct anagrams of s. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "too hot"
Output: 18
Explanation: Some of the anagrams of the given string are "too hot", "oot hot", "oto toh", "too toh", and "too oht".
Example 2:

Input: s = "aa"
Output: 1
Explanation: There is only one anagram possible for the given string. """

import math


class Solution:
    def countAnagrams(self, s: str) -> int:
        def countPermutation(s):
            # 计算一个单词的排列数
            # 例如：aab，有3个a，2个b，那么排列数为3!/(2!1!) = 3
            lens = len(s)
            # 除以相同字母的阶乘
            # 计算每个字母出现的次数
            count = {}
            for i in s:
                if i not in count:
                    count[i] = 1
                else:
                    count[i] += 1
            # 计算阶乘
            factorial = 1
            for i in count.values():
                factorial *= math.factorial(i)
            return (math.factorial(lens) // factorial) % (10 ** 9 + 7)

        # 计算一个字符串的排列数
        res = 1
        words = s.split()
        for word in words:
            res *= countPermutation(word)
        return res % (10 ** 9 + 7)

print(Solution().countAnagrams("too hot"))

        