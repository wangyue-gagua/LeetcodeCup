/* A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls. Since the answer may be too large, return it modulo 109 + 7.

Two sequences are considered different if at least one element differs from each other.

 

Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
Example 2:

Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30
Example 3:

Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181 */

function dieSimulator(n: number, rollMax: number[]): number {
    // 动态规划解决
    // dp[i][j][k]表示第i次掷骰子，第i次掷出的数字为j，且连续出现的次数为k的方案数
    // dp[i][j][k] = dp[i - 1][j][k - 1] k > 1
    // dp[i][j][k] = sum(dp[i - 1][j][k - 1]) k = 1
    // dp[i][j][k] = k > rollMax[j] dp[i][j][k] = 0

    const mod = 1e9 + 7;
    const dp: number[][][] = new Array(n + 1);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(6);
        for (let j = 0; j < 6; j++) {
            dp[i][j] = new Array(16).fill(0);
        }
    }
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < 6; j++) {
            for (let k = 1; k <= rollMax[j]; k++) {
                if (i === 1) {
                    dp[i][j][k] = 1;
                } else {
                    for (let m = 0; m < 6; m++) {
                        if (m === j) {
                            dp[i][j][k] += dp[i - 1][m][k - 1];
                        } else {
                            dp[i][j][k] += dp[i - 1][m][rollMax[m]];
                        }
                        dp[i][j][k] %= mod;
                    }
                }
            }
        }
    }
    let res = 0;
    for (let i = 0; i < 6; i++) {
        res += dp[n][i][rollMax[i]];
        res %= mod;
    }
    return res;
};

console.log(dieSimulator(2, [1, 1, 2, 2, 2, 3]));
console.log(dieSimulator(2, [1, 1, 1, 1, 1, 1]));
console.log(dieSimulator(3, [1, 1, 1, 2, 2, 3]));