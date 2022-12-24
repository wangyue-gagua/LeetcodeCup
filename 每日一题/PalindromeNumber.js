/* Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not. */

/**
 * @param {number} x
 * @return {boolean}
 */
 var isPalindrome = function(x) {
    let xStr = x.toString();
    let xStrRev = xStr.split('').reverse().join('');
    return xStr === xStrRev;

};