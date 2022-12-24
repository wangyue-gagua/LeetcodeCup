// function longestPalindrome(s: string): string {
//     // Initialize the longest palindrome seen so far
//     let max_palindrome = "";

//     // Iterate over the characters in the string
//     for (let i = 0; i < s.length; i++) {
//         // Expand outwards from the current character to find the longest palindrome that includes it as the center
//         let left = i;
//         let right = i;
//         while (left >= 0 && s[left] === s[i]) {
//             left--;
//         }
//         while (right < s.length && s[right] === s[i]) {
//             right++;
//         }
//         while (left >= 0 && right < s.length && s[left] === s[right]) {
//             left--;
//             right++;
//         }
//         left++;
//         right--;

//         // Update the longest palindrome seen so far if the current palindrome is longer
//         if (right - left + 1 > max_palindrome.length) {
//             max_palindrome = s.substring(left, right + 1);
//         }
//     }

//     return max_palindrome;
// }

// // Test the function
// console.log(longestPalindrome("abccbca"));  // Should print "abccba"
// console.log(longestPalindrome("abcdefg"));  // Should print "a"
// console.log(longestPalindrome("a"));  // Should print "a"

// manacher's algorithm
function longestPalindrome(s: string): string {
    if (s.length < 2) return s;
    const str = `#${s.split('').join('#')}#`;
    const p = new Array(str.length).fill(0);
    let maxRight = 0, center = 0;
    let maxLen = 0, start = 0;
    for (let i = 0; i < str.length; i++) {
        if (i < maxRight) {
            const mirror = 2 * center - i;
            p[i] = Math.min(maxRight - i, p[mirror]);
        }
        let left = i - (1 + p[i]), right = i + (1 + p[i]);
        while (left >= 0 && right < str.length && str[left] === str[right]) {
            p[i]++;
            left--;
            right++;
        }
        if (i + p[i] > maxRight) {
            maxRight = i + p[i];
            center = i;
        }
        if (p[i] > maxLen) {
            maxLen = p[i];
            start = (i - maxLen) / 2;
        }
    }
    return s.substring(start, start + maxLen);
}