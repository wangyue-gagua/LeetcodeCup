/**
 * @param {number[]} digits
 * @return {number[]}
 */
 var plusOne = function(digits) {
    if (digits.length === 1 && digits[0] === 9) {
        return [1, 0]
    } else if (digits.length === 1) {
        let res = digits[digits.length - 1] + 1;
        return [res]
    } else if (digits[digits.length - 1] === 9) {
        let res = plusOne(digits.slice(0, digits.length - 1))
        res.push(0)
        return res
    } else {
        let res = digits.slice(0, digits.length - 1)
        console.log(res)
        res.push(digits[digits.length - 1] + 1)
        return res
    }
};

console.log(plusOne([1, 2, 3]))