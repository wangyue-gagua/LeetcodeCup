/* You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3 */

function maxValue(n: number, index: number, maxSum: number): number {
    let left = 0;
    let right = maxSum;
    while (left < right) {
        const mid = Math.floor((left + right + 1) / 2);
        if (check(mid, n, index, maxSum)) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    return left - 1;
};

function check(mid: number, n: number, index: number, maxSum: number) {
    let sum = mid;
    let l = index;
    let r = index;
    let num = mid - 1;
    while (l > 0 || r < n - 1) {
        if (l > 0) {
            l--;
            sum += num;
            num--;
        }
        if (r < n - 1) {
            r++;
            sum += num;
            num--;
        }
    }
    return sum <= maxSum;
}

console.log(maxValue(4, 2, 6));
console.log(maxValue(6, 1, 10));