/* 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。

每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。

如果无法让 arr1 严格递增，请返回 -1。

 

示例 1：

输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
输出：1
解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
示例 2：

输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
输出：2
解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
示例 3：

输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
输出：-1
解释：无法使 arr1 严格递增。
 

提示：

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9 */

function makeArrayIncreasing(arr1: number[], arr2: number[]): number {
    const arr2Set = new Set(arr2);
    arr2 = [...arr2Set];
    arr2.sort((a, b) => a - b);
    const len1 = arr1.length;
    const len2 = arr2.length;
    const dp: number[][] = new Array(len1).fill(0).map(() => new Array(len2 + 1).fill(Infinity));
    dp[0][0] = 0;
    for (let i = 1; i < len1; i++) {
        dp[i][0] = arr1[i] > arr1[i - 1] ? dp[i - 1][0] : Infinity;
        for (let j = 1; j <= len2; j++) {
            if (arr1[i] > arr1[i - 1]) {
                dp[i][j] = Math.min(dp[i][j], dp[i - 1][j]);
            }
            if (arr1[i] > arr2[j - 1]) {
                dp[i][j] = Math.min(dp[i][j], dp[i - 1][j - 1] + 1);
            }
            if (arr2[j - 1] > arr1[i - 1]) {
                dp[i][j] = Math.min(dp[i][j], dp[i - 1][0] + 1);
            }
        }
    }
    return Math.min(...dp[len1 - 1]);
};

console.log(makeArrayIncreasing([1, 5, 3, 6, 7], [1, 3, 2, 4]));
console.log(makeArrayIncreasing([1, 5, 3, 6, 7], [4, 3, 1]));
console.log(makeArrayIncreasing([1, 5, 3, 6, 7], [1, 6, 3, 3]));