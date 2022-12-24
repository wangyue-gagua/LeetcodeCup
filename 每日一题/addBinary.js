/* Given two binary strings a and b, return their sum as a binary string. */

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
 var addBinary = function(a, b) {
    let result = [];
    let carry = 0;
    let i = a.length - 1;
    let j = b.length - 1;
    while (i >= 0 || j >= 0) {
        let sum = carry;
        if (j >= 0) {
            sum += b[j] - '0';
            j--;
        }
        if (i >= 0) {
            sum += a[i] - '0';
            i--;
        }
        result.push(sum % 2);
        carry = Math.floor(sum / 2);
    }
    if (carry != 0) {
        result.push(carry);
    }
    return result.reverse().join('');
};