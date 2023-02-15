/* Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.

Return True if the array is good otherwise return False.

 

Example 1:

Input: nums = [12,5,7,23]
Output: true
Explanation: Pick numbers 5 and 7.
5*3 + 7*(-2) = 1
Example 2:

Input: nums = [29,6,10]
Output: true
Explanation: Pick numbers 29, 6 and 10.
29*1 + 6*(-3) + 10*(-1) = 1
Example 3:

Input: nums = [3,6]
Output: false
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9 */

function isGoodArray(nums: number[]): boolean {
    // gcd(a, b) === 1

    // 1. 暴力法
    // 2. 求最大公约数

    return arrayGcd(nums) === 1;

};

function gcd(a: number, b: number): number {
    if (a === 0) {
        return b;
    }
    return gcd(b % a, a);
}

function arrayGcd(nums: number[]): number {
    let result = nums[0];
    for (let i = 1; i < nums.length; i++) {
        result = gcd(result, nums[i]);
    }
    return result;
}

console.log(isGoodArray([12, 5, 7, 23]));
console.log(isGoodArray([29, 6, 10]));
console.log(isGoodArray([3, 6]));