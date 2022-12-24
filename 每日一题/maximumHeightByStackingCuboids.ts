/* Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

Return the maximum height of the stacked cuboids.

 

Example 1:



Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
Output: 190
Explanation:
Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
Cuboid 0 is placed next with the 45x20 side facing down with height 50.
Cuboid 2 is placed next with the 23x12 side facing down with height 45.
The total height is 95 + 50 + 45 = 190.
Example 2:

Input: cuboids = [[38,25,45],[76,35,3]]
Output: 76
Explanation:
You can't place any of the cuboids on the other.
We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.
Example 3:

Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
Output: 102
Explanation:
After rearranging the cuboids, you can see that all cuboids have the same dimension.
You can place the 11x7 side down on all cuboids so their heights are 17.
The maximum height of stacked cuboids is 6 * 17 = 102. */

function maxHeight(cuboids: number[][]): number {
    const n = cuboids.length;
    for (const cuboid of cuboids) {
        cuboid.sort((a, b) => a - b);
    }
    cuboids.sort((a, b) => {
        if (a[0] === b[0]) {
            if (a[1] === b[1]) {
                return a[2] - b[2];
            }
            return a[1] - b[1];
        }
        return a[0] - b[0];
    });
    const dp = new Array(n).fill(0);
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        dp[i] = cuboids[i][2];
        for (let j = 0; j < i; ++j) {
            if (cuboids[j][0] <= cuboids[i][0] && cuboids[j][1] <= cuboids[i][1] && cuboids[j][2] <= cuboids[i][2]) {
                dp[i] = Math.max(dp[i], dp[j] + cuboids[i][2]);
            }
        }
        ans = Math.max(ans, dp[i]);
    }
    return ans;
};

console.log(maxHeight([[29,59,36],[12,13,97],[49,86,43],[9,57,50],[97,19,10],[17,92,69],[92,36,15],[16,63,8],[94,24,78],[52,11,39],[48,61,57],[15,44,79],[6,69,98],[30,70,41],[23,17,33],[85,86,12],[13,75,98],[75,30,30],[89,18,27],[94,83,81]]));