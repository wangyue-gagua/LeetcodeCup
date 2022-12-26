/* Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
Example 2:

Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
Example 3:

Input: s = "zzzzz"
Output: 15 */

function countHomogenous(s: string): number {
    // 记录当前相同字符的个数
    // n个相同字符串的贡献为n*(n+1)/2
    let sameCharCount = 1
    let res = 0
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i - 1]) {
            sameCharCount++
        } else {
            res += ((sameCharCount * (sameCharCount + 1)) / 2) % (10 ** 9 + 7)
            sameCharCount = 1
        }
    }
    // 最后一个字符结算
    res += ((sameCharCount * (sameCharCount + 1)) / 2) % (10 ** 9 + 7)
    return res % (10 ** 9 + 7)

};