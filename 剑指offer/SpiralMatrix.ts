// Given an m x n matrix, return all elements of the matrix in spiral order.
function spiralOrder(matrix: number[][]): number[] {
    if (matrix.length === 0) return [];
    const m = matrix.length;
    const n = matrix[0].length;
    const res = [];
    let left = 0, right = n - 1, top = 0, bottom = m - 1;
    while (left <= right && top <= bottom) {
        for (let i = left; i <= right; i++) {
            res.push(matrix[top][i]);
        }
        for (let i = top + 1; i <= bottom; i++) {
            res.push(matrix[i][right]);
        }
        if (left < right && top < bottom) {
            for (let i = right - 1; i > left; i--) {
                res.push(matrix[bottom][i]);
            }
            for (let i = bottom; i > top; i--) {
                res.push(matrix[i][left]);
            }
        }
        left++;
        right--;
        top++;
        bottom--;
    }
    return res;
};