/* You are given a string text. You should split it to k substrings (subtext1, subtext2, ..., subtextk) such that:

subtexti is a non-empty string.
The concatenation of all the substrings is equal to text (i.e., subtext1 + subtext2 + ... + subtextk == text).
subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).
Return the largest possible value of k.

 

Example 1:

Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
Example 2:

Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".
Example 3:

Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".
 

Constraints:

1 <= text.length <= 1000
text consists only of lowercase English characters. */

function longestDecomposition(text: string): number {
    // 最后一个字符为char, 从头开始找到第一个char, 如果找到了, 则判断前后是否相等, 如果相等, 则继续找
    const lens = text.length;
    if (lens === 0) return 0;
    if (lens === 1) return 1;
    let maxIndex = 0
    for (let i = 0; i < Math.floor(lens / 2); i++) {
        if (text[i] === text[lens - 1]) {
            if (text.slice(0, i + 1) === text.slice(lens - i - 1)) {
                maxIndex = i + 1
                break
            }
        }
    }
    if (maxIndex === 0) {
        return 1
    } else {
        return 2 + longestDecomposition(text.slice(maxIndex, lens - maxIndex))
    }
};

// console.log(longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"));
// console.log(longestDecomposition("merchant"));
// console.log(longestDecomposition("antaprezatepzapreanta"));
console.log(longestDecomposition("elvtoelvto"));