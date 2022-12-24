/* 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36 */

function cuttingRope(n: number): number {
    // dp[N]表示N米绳子的最大乘积
    // dp[n] = max{x * dp[n-x] }
    const dp = new Array(n + 1).fill(0)
    dp[1] = 1
    dp[2] = 1
    for (let i = 3; i <= n; i++) {
        for (let j = 2; j < i; j++) {
            dp[i] = Math.max(dp[i], j * Math.max(i - j, dp[i - j]))
        }
    }
    // console.log(dp)
    return dp[n]
};

console.log(cuttingRope(10))