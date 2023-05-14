/* 在一个无限的 x 坐标轴上，有许多水果分布在其中某些位置。给你一个二维整数数组 fruits ，其中 fruits[i] = [positioni, amounti] 表示共有 amounti 个水果放置在 positioni 上。fruits 已经按 positioni 升序排列 ，每个 positioni 互不相同 。

另给你两个整数 startPos 和 k 。最初，你位于 startPos 。从任何位置，你可以选择 向左或者向右 走。在 x 轴上每移动 一个单位 ，就记作 一步 。你总共可以走 最多 k 步。你每达到一个位置，都会摘掉全部的水果，水果也将从该位置消失（不会再生）。

返回你可以摘到水果的 最大总数 。

 

示例 1：


输入：fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
输出：9
解释：
最佳路线为：
- 向右移动到位置 6 ，摘到 3 个水果
- 向右移动到位置 8 ，摘到 6 个水果
移动 3 步，共摘到 3 + 6 = 9 个水果
示例 2：


输入：fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
输出：14
解释：
可以移动最多 k = 4 步，所以无法到达位置 0 和位置 10 。
最佳路线为：
- 在初始位置 5 ，摘到 7 个水果
- 向左移动到位置 4 ，摘到 1 个水果
- 向右移动到位置 6 ，摘到 2 个水果
- 向右移动到位置 7 ，摘到 4 个水果
移动 1 + 3 = 4 步，共摘到 7 + 1 + 2 + 4 = 14 个水果
示例 3：


输入：fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
输出：0
解释：
最多可以移动 k = 2 步，无法到达任一有水果的地方 */

function maxTotalFruits(fruits: number[][], startPos: number, k: number): number {
    // 还是要用前缀和 计算区间内的水果总数
    let fruitsMax = fruits[fruits.length - 1][0];
    fruitsMax = Math.max(fruitsMax, startPos);
    const prefix = new Array(fruitsMax + 1).fill(0);
    for (let [pos, cnt] of fruits) {
        prefix[pos] = cnt;
    }
    for (let i = 1; i <= fruitsMax; i++) {
        prefix[i] += prefix[i - 1];
    }
    let max = 0;
    // 往左走
    const leftMostPos = Math.max(0, startPos - k);
    let regionLeft: number
    if (leftMostPos > 0) {
        regionLeft = prefix[startPos] - prefix[leftMostPos - 1];
    } else {
        regionLeft = prefix[startPos];
    }
    max = Math.max(max, regionLeft);
    // 往右走
    const rightMostPos = Math.min(fruitsMax, startPos + k);
    let regionRight: number
    if (startPos === 0) {
        regionRight = prefix[rightMostPos];
    } else {
        regionRight = prefix[rightMostPos] - prefix[startPos - 1];
    }
    // console.log(regionRight, "right")
    max = Math.max(max, regionRight);
    // 先左后右
    // 最多往左走k // 2步，再往右走剩下的步数
    for (let i = 0; i <= Math.floor(k / 2) ; i++) {
        const leftPos = Math.max(0, startPos - i);
        const rightPos = Math.min(fruitsMax, startPos + k - i * 2);
        let region : number
        if (leftPos === 0) {
            region = prefix[rightPos];
        } else {
            region = prefix[rightPos] - prefix[leftPos - 1];
        }
        // console.log(region, "LTR")
        max = Math.max(max, region);
    }
    // 先右后左
    // 最多往右走k // 2步，再往左走剩下的步数
    for (let i = 0; i <= Math.floor(k / 2) ; i++) {
        const rightPos = Math.min(fruitsMax, startPos + i);
        const leftPos = Math.max(0, startPos - k + i * 2);
        let region : number
        if (leftPos === 0) {
            region = prefix[rightPos];
        } else {
            region = prefix[rightPos] - prefix[leftPos - 1];
        }
        max = Math.max(max, region);
    }
    // console.log(prefix);
    return max;
};

// console.log(maxTotalFruits([[2,8],[6,3],[8,6]], 5, 4));
// console.log(maxTotalFruits([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], 5, 4));
// console.log(maxTotalFruits([[0,3],[6,4],[8,5]], 3, 2));

// console.log(maxTotalFruits([[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]], 21, 30));

const tst = [[0,10],[1,6],[2,4],[8,10],[9,5],[13,3],[14,3],[23,4],[28,5],[29,7],[30,6],[32,2],[33,8],[36,4],[40,9]]
console.log(maxTotalFruits(tst, 0, 23));