/* 给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。

子数组 是数组中 连续 的一部分。 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var shortestSubarray = function(nums, k) {
    let sum = nums.reduce((a, b) => a +b, 0)
    console.log(sum)
    let len = nums.length
    let left = 0
    let right = len - 1
    if (len === 1) return 1
    while (left < right) {
        if (nums[left] < nums[right] && sum - nums[left] >= k) {
            len -= 1
            sum -= nums[left]
            left++
        } else if (nums[left] >= nums[right] && sum - nums[right] >= k) {
            len -= 1
            sum -= nums[right]
            right--
        } else {
            return len
        }
        
    }
    return len

};

console.log(shortestSubarray([17,85,93,-45,-21], 150))