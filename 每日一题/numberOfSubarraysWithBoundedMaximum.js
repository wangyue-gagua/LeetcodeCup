/* Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Example 2:

Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7 */

/**
 * @param {number[]} nums
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var numSubarrayBoundedMax = function (nums, left, right) {
    // dp[i] 表示以 nums[i] 结尾的符合条件的子数组的个数
    // dp[i] = dp[i - 1] + 1
    const dp = new Array(nums.length).fill(0);
    let res = 0;
    if (nums[0] >= left && nums[0] <= right) {
        dp[0] = 1;
        res++;
    }
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] <= right) {
            if (nums[i] >= left) {
                let j = i - 1;
                dp[i] = dp[i - 1] + 1;
                while (j >= 0 && nums[j] < left) {
                    dp[i]++;
                    j--;
                    // console.log(i)
                }
            } else {
                dp[i] = dp[i - 1];
            }
        }
        res += dp[i];
    }
    // console.log(dp);
    return res;
};

console.log(
    numSubarrayBoundedMax([73, 55, 36, 5, 55, 14, 9, 7, 72, 52], 32, 69)
);
