/* You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's. */

/**
 * @param {number} n
 * @param {number[][]} mines
 * @return {number}
 */
var orderOfLargestPlusSign = function (n, mines) {
    if (mines.length == n * n) {
        return 0;
    }
/*     const minesSet = new Set();
    for (const [x, y] of mines) {
        minesSet.add(`${x},${y}`);
    }
    const isValidK = (k, x, y) => {
        for (let i = 0; i < k; i++) {
            if (
                minesSet.has(`${x + i},${y}`) ||
                minesSet.has(`${x - i},${y}`) ||
                minesSet.has(`${x},${y + i}`) ||
                minesSet.has(`${x},${y - i}`)
            )
                return false;
        }
        return true;
    };
    // let res = Math.ceil(n / 2);
    // for (let k = Math.floor((n + 1) / 2); k > 0; k--) {
    //     for (let i = k-1; i < n - k + 1; i++) {
    //         for (let j = k-1; j < n - k + 1; j++) {
    //             if (minesSet.has(`${i},${j}`)) continue;
    //             if (isValidK(k, i, j)) {
    //                 return k;
    //             }
    //         }
    //     }
    // }
    const checkValidK = (k) => {
        for (let i = k - 1; i < n - k + 1; i++) {
            for (let j = k - 1; j < n - k + 1; j++) {
                // console.log(k, i, j);
                if (minesSet.has(`${i},${j}`)) continue;
                if (isValidK(k, i, j)) {
                    return true;
                }
            }
        }
        return false;
    };
    let k = 2
    while (k <= Math.floor((n + 1) / 2)) {
        if (checkValidK(k)) {
            k++;
        } else {
            break;
        }
    }
    return k - 1; */

    //dp
    const minesSet = new Set();
    for (const [x, y] of mines) {
        minesSet.add(`${x},${y}`);
    }
    const dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        let count = 0;
        for (let j = 0; j < n; j++) {
            count = minesSet.has(`${i},${j}`) ? 0 : count + 1;
            dp[i][j] = count;
        }
        count = 0;
        for (let j = n - 1; j >= 0; j--) {
            count = minesSet.has(`${i},${j}`) ? 0 : count + 1;
            dp[i][j] = Math.min(dp[i][j], count);
        }
    }
    for (let j = 0; j < n; j++) {
        let count = 0;
        for (let i = 0; i < n; i++) {
            count = minesSet.has(`${i},${j}`) ? 0 : count + 1;
            dp[i][j] = Math.min(dp[i][j], count);
        }
        count = 0;
        for (let i = n - 1; i >= 0; i--) {
            count = minesSet.has(`${i},${j}`) ? 0 : count + 1;
            dp[i][j] = Math.min(dp[i][j], count);
        }
    }
    let res = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            res = Math.max(res, dp[i][j]);
        }
    }
    return res;
}
console.log(
    orderOfLargestPlusSign(3, [[0, 0]]))