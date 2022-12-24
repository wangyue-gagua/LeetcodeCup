/* You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile. */

/**
 * @param {number} n
 * @return {number}
 */
var numTilings = function (n) {
    if (n === 1) return 1;
    if (n === 2) return 2;
    // a[n][n] = a[n-1][n-1] + a[n-1][n-2] + a[n-2][n-1] + a[n-2][n-2]
    // a[n][n+1] = a[n-1][n-1] + a[n][n-1] 
    // a[n+1][n] = a[n-1][n-1] + a[n-1][n]
    const mod = 10 ** 9 + 7;
    const a = new Array(n + 1).fill(1).map(() => new Array(n + 1).fill(1));
    a[1][1] = 1;
    a[1][2] = 1;
    a[2][1] = 1;
    a[2][2] = 2;
    a[2][3] = 2;
    a[3][2] = 2;

    for (let i = 3; i < n; i++) {
        a[i][i] = (a[i - 1][i - 1] + a[i - 1][i - 2] + a[i - 2][i - 1] + a[i - 2][i - 2]) % mod;
        a[i][i + 1] = (a[i - 1][i - 1] + a[i][i - 1]) % mod;
        a[i + 1][i] = (a[i - 1][i - 1] + a[i - 1][i]) % mod;
    }
    a[n][n] = (a[n - 1][n - 1] + a[n - 1][n - 2] + a[n - 2][n - 1] + a[n - 2][n - 2]) % mod;
    


    // console.log(a);
    return a[n][n];
};

console.log(numTilings(5));
