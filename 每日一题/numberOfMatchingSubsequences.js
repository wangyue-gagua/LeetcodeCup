/* Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2 */

/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
 var numMatchingSubseq = function(s, words) {
    const charIndexMap = {}
    for (let i = 0; i < s.length; i++) {
        const char = s[i]
        if (!charIndexMap[char]) {
            charIndexMap[char] = [i]
        } else {
            charIndexMap[char].push(i)
        }
    }
    let count = 0
    console.log(charIndexMap)
    function isSubsequence(word) {
        let prevIndex = -1
        let i = 0
        while (i < word.length) {
            const char = word[i]
            if (!charIndexMap[char]) {
                return false
            } else {
                const index = binarySearch(charIndexMap[char], prevIndex)
                if (index === -1) {
                    return false
                } else {
                    prevIndex = charIndexMap[char][index] + 1
                    // console.log(prevIndex)
                    i++
                }
            }
        }
        return true
    }
    for (const word of words) {
        if (isSubsequence(word)) {
            count++
        }
    }
    return count
};

// 二分查找第一个大于等于target的数的索引，如果没有返回-1
function binarySearch(arr, target) {
    let left = 0
    let right = arr.length - 1
    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2)
        if (arr[mid] >= target) {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return left === arr.length ? -1 : left
}


// console.log(binarySearch([0, 2, 3, 4, 5, 6, 7, 8, 9], 1))
console.log(numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))