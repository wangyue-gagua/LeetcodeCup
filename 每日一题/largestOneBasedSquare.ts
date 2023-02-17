/* Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

 

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1
 

Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1 */

function largest1BorderedSquare(grid: number[][]): number {
    // 统计每个点上下左右的连续1的个数

    const row = grid.length;
    const col = grid[0].length;

    const left = new Array(row).fill(0).map(() => new Array(col).fill(0));
    const right = new Array(row).fill(0).map(() => new Array(col).fill(0));
    const top = new Array(row).fill(0).map(() => new Array(col).fill(0));
    const bottom = new Array(row).fill(0).map(() => new Array(col).fill(0));

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (grid[i][j] === 1) {
                left[i][j] = (j === 0 ? 0 : left[i][j - 1]) + 1;
                top[i][j] = (i === 0 ? 0 : top[i - 1][j]) + 1;
            }
        }
    }

    for (let i = row - 1; i >= 0; i--) {
        for (let j = col - 1; j >= 0; j--) {
            if (grid[i][j] === 1) {
                right[i][j] = (j === col - 1 ? 0 : right[i][j + 1]) + 1;
                bottom[i][j] = (i === row - 1 ? 0 : bottom[i + 1][j]) + 1;
            }
        }
    }

    // 对于边长为k的正方形，它的左上角坐标为(i, j)，那么它的右下角坐标为(i + k - 1, j + k - 1)
    // (i, j)的右边长为right[i][j], 下边长为bottom[i][j]
    // (i + k - 1, j + k - 1)的左边长为left[i + k - 1][j + k - 1], 上边长为top[i + k - 1][j + k - 1]

    for (let k = Math.min(row, col); k >= 1; k--) {
        for (let i = 0; i <= row - k; i++) {
            for (let j = 0; j <= col - k; j++) {
                if (left[i + k - 1][j + k - 1] >= k && right[i][j] >= k && top[i + k - 1][j + k - 1] >= k && bottom[i][j] >= k) {
                    return k * k;
                }
            }
        }
    }

    return 0;
};

console.log(largest1BorderedSquare([[1, 1, 1], [1, 0, 1], [1, 1, 1]]));
console.log(largest1BorderedSquare([[1, 1, 0, 0]]));