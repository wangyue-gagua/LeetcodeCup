/* 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0 */

function longestValidParentheses(s: string): number {
    let leftBracket = 0
    let rightBracket = 0
    let tempScore = 0
    let res = 0
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            leftBracket++
        } else {
            rightBracket++
        }
        if (leftBracket === rightBracket) {
            tempScore = leftBracket * 2
            res = Math.max(res, tempScore)
        } else if (rightBracket > leftBracket) {
            leftBracket = 0
            rightBracket = 0
            tempScore = 0
        }
    }
    leftBracket = 0
    rightBracket = 0
    tempScore = 0
    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] === '(') {
            leftBracket++
        } else {
            rightBracket++
        }
        if (leftBracket === rightBracket) {
            tempScore = leftBracket * 2
            res = Math.max(res, tempScore)
        } else if (leftBracket > rightBracket) {
            leftBracket = 0
            rightBracket = 0
            tempScore = 0
        }
    }
    return res
};

console.log(longestValidParentheses(")()())"))