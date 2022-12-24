/* You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1. */


/**
 * @param {string[]} grid
 * @return {number}
 */
 var shortestPathAllKeys = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const keys = new Set();
    const locks = new Set();
    let start = null;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const c = grid[i][j];
            if (c === '@') {
                start = [i, j];
            } else if (c >= 'a' && c <= 'f') {
                keys.add(c);
            } else if (c >= 'A' && c <= 'F') {
                locks.add(c);
            }
        }
    }
    const visited = new Set();
    const queue = [[start[0], start[1], 0, new Set()]];
    visited.add(`${start[0]},${start[1]},${0}`);
    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    let res = 0;
    while (queue.length) {
        const size = queue.length;
        for (let i = 0; i < size; i++) {
            const [x, y, step, keySet] = queue.shift();
            if (keys.size === keySet.size) {
                return res;
            }
            for (const [dx, dy] of dirs) {
                const nx = x + dx;
                const ny = y + dy;
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                const c = grid[nx][ny];
                if (c === '#') continue;
                const newKeySet = new Set(keySet);
                if (c >= 'a' && c <= 'f') {
                    newKeySet.add(c);
                }
                if (c >= 'A' && c <= 'F') {
                    if (!newKeySet.has(c.toLowerCase())) continue;
                }
                const key = `${nx},${ny},${[...newKeySet].sort().join('')}`;
                if (visited.has(key)) continue;
                visited.add(key);
                queue.push([nx, ny, step + 1, newKeySet]);
            }
        }
        res++;
    }
    return -1;
};