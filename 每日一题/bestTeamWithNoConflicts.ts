/* You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 

Example 1:

Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.
Example 2:

Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
Example 3:

Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players. 
 

Constraints:

1 <= scores.length, ages.length <= 1000
scores.length == ages.length
1 <= scores[i] <= 106
1 <= ages[i] <= 1000 */

function bestTeamScore(scores: number[], ages: number[]): number {
    // conflict即年龄小的有更大的得分
    // 用一个变量记录之前的最大得分
    // 将年龄和得分一一对应，按年龄排序、
    // 年龄相同时， 得分由小到大排序
    const scoreAge = [];
    for (let i = 0; i < scores.length; i++) {
        scoreAge.push([scores[i], ages[i]]);
    }
    scoreAge.sort((a, b) => {
        if (a[1] === b[1]) {
            return a[0] - b[0];
        }
        return a[1] - b[1];
    });
    // dp[i]表示当前i为止的最大总得分以及单个最大分数的位置
    //
    const dp = new Array(scores.length + 1).fill(0).map(() => new Array(2).fill(0));
    dp[1] = [scoreAge[0][0], 0];
    for (let i = 2; i <= scores.length; i++) {
        dp[i][0] = scoreAge[i - 1][0];
        dp[i][1] = i - 1;
        for (let j = i - 1; j >= 0; j--) {
            // 单个最大分数要小于当前分数
            const prevAgeIndex = dp[j][1];
            const prevAge = scoreAge[prevAgeIndex][1];
            const curAge = scoreAge[i - 1][1];
            if (prevAge === curAge) {
                if (dp[j][0] + scoreAge[i - 1][0] > dp[i][0]) {
                    dp[i] = [dp[j][0] + scoreAge[i - 1][0], i - 1];
                }
            }
            if (prevAge < curAge) {
                const prevIndexScore = scoreAge[prevAgeIndex][0];
                if (prevIndexScore <= scoreAge[i - 1][0]) {
                    if (dp[j][0] + scoreAge[i - 1][0] > dp[i][0]) {
                        dp[i][0] = dp[j][0] + scoreAge[i - 1][0];
                        if (prevIndexScore === scoreAge[i - 1][0]) {
                            dp[i][1] = prevAgeIndex;
                        } else {
                            dp[i][1] = i - 1;
                        }
                    }
                }
            }
        }
    }

    let maxRes = 0
    for (let i of dp) {
        if (i[0] > maxRes) {
            maxRes = i[0]
        }
    }
    return maxRes
}

// console.log(bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]));
// console.log(bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]));
// console.log(bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]));

// console.log(bestTeamScore([1,1,1,1,1,1,1,1,1,1], [811,364,124,873,790,656,581,446,885,134]))
// console.log(bestTeamScore([9,2,8,8,2], [4,1,3,3,5]))

console.log(bestTeamScore([1,3,7,3,2,4,10,7,5], [4,5,2,1,1,2,4,1,4]))