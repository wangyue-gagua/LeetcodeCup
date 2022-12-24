/* Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Example 2:

Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7 */

function numSubarrayBoundedMax(nums: number[], left: number, right: number): number {
    // 单调栈
    let n = nums.length;
    let lArr = new Array<number>(n).fill(-1);
    let rArr = new Array<number>(n).fill(n);
    let stack: number[] = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] < nums[i]) {
            let val = stack.pop() as number;
            rArr[val] = i;
        }
        stack.push(i);
    }
    stack = [];
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && nums[stack[stack.length - 1]] <= nums[i]) {
            let val = stack.pop() as number;
            lArr[val] = i;
        }
        stack.push(i);
    }
    let res = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] >= left && nums[i] <= right) {
            res += (i - lArr[i]) * (rArr[i] - i);
        }
    }
    return res;
};

console.log(numSubarrayBoundedMax([2,1,4,3], 2, 3));