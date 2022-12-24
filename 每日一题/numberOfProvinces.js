/* There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3 */

/**
 * @param {number[][]} isConnected
 * @return {number}
 */
 var findCircleNum = function(isConnected) {
    const cityConnectedMap = new Map()
    const len = isConnected.length
    for (let i = 0; i < len; i++) {
        for (let j = 0; j < len; j++) {
            if (isConnected[i][j] === 1) {
                if (cityConnectedMap.has(i)) {
                    cityConnectedMap.get(i).push(j)
                } else {
                    cityConnectedMap.set(i, [j])
                }
            }
        }
    }
    // console.log(cityConnectedMap.entries())
    const searchedArr = new Array(len).fill(false)
    let res = 0
    for (let i = 0; i < len; i++) {
        if (!searchedArr[i]) {
            searchedArr[i] = true
            const queue = cityConnectedMap.get(i)
            // console.log(queue)
            while (queue.length > 0) {
                const index = queue.pop()
                if (!searchedArr[index]) {
                    queue.push(...cityConnectedMap.get(index))
                    searchedArr[index] = true
                }
            }
            res++
        }
    }
    return res
};

console.log(findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))