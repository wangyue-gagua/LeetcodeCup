/* The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

 

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17 */

function beautySum(s: string): number {
    const sFreqArr = new Array(s.length)
        .fill(0)
        .map(() => new Array(26).fill(0));
    for (let i = 0; i < s.length; i++) {
        sFreqArr[i][s.charCodeAt(i) - 97]++;
        if (i > 0) {
            for (let j = 0; j < 26; j++) {
                sFreqArr[i][j] += sFreqArr[i - 1][j];
            }
        }
    }
    let res = 0;
    for (let i = 0; i < s.length; i++) {
        for (let j = i; j < s.length; j++) {
            let min = Infinity;
            let max = -Infinity;
            for (let k = 0; k < 26; k++) {
                const freq = sFreqArr[j][k] - (i > 0 ? sFreqArr[i - 1][k] : 0);
                if (freq > 0) {
                    min = Math.min(min, freq);
                    max = Math.max(max, freq);
                }
            }
            res += max - min;
        }
    }
    return res;
}

console.log(
    beautySum(
        "xbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbbxbb"
    )
);
