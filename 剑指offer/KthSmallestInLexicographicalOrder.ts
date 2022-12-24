/* Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1 */

function findKthNumber(n: number, k: number): number {
    // 直接排序当然会超时 1 <= k <= n <= 109
    // const arr = new Array(n).fill(0)
    // for (let i = 0; i < n; i++) {
    //     arr[i] = i + 1
    // }
    // arr.sort()
    // return arr[k - 1]

    // fast method
    // 1. 从1开始，每次乘10，直到大于n，然后回退一步，变成9
    // 2. 从9开始，每次减1，直到小于n，然后回退一步，变成8
    // 3. 重复1和2，直到k为0
    let cur = 1;
    k--;
    while (k > 0) {
        let steps = calSteps(n, cur, cur + 1);
        console.log(steps)
        if (steps <= k) {
            cur++;
            k -= steps;
        } else {
            cur *= 10;
            k--;
        }
    }
    return cur;
};

function calSteps(n: number, n1: number, n2: number): number {
    let steps = 0;
    while (n1 <= n) {
        steps += Math.min(n + 1, n2) - n1;
        n1 *= 10;
        n2 *= 10;
    }
    return steps;
}

console.log(findKthNumber(13, 2))