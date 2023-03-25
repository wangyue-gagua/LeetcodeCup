/* 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。

一个子数组指的是原数组中连续的一个子序列。

请你返回满足题目要求的最短子数组的长度。

 

示例 1：

输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。
示例 2：

输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
示例 3：

输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。
示例 4：

输入：arr = [1]
输出：0
 

提示：

1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9 */

function findLengthOfShortestSubarray(arr: number[]): number {
    const n = arr.length;
    // 切头
    let right = n - 1;
    while (right > 0 && arr[right - 1] <= arr[right]) {
        right--;
    }
    if (right === 0) {
        return 0;
    }
    let ans = right;
    // 切尾
    let left = 0;
    while (left < right && arr[left] <= arr[left + 1]) {
        left++;
    }
    ans = Math.min(ans, n - left - 1);
    // 切中
    function binarySearch(left: number, right: number, target: number) {
        // 找到第一个大于等于target的数
        let ans = n;
        while (left <= right) {
            const mid = (left + right) >> 1;
            if (arr[mid] >= target) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
    for (let i = 0; i <= left; i++) {
        const index = binarySearch(right, n - 1, arr[i]);
        // 判断是否有大于等于arr[i]的数
        if (index < n) {
            ans = Math.min(ans, index - i - 1);
        }
    }
    return ans;
};

console.log(findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))
console.log(findLengthOfShortestSubarray([5,4,3,2,1]))
console.log(findLengthOfShortestSubarray([1,2,3]))
console.log(findLengthOfShortestSubarray([1]))
