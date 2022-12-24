/* There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B,
Serve 75 ml of soup A and 25 ml of soup B,
Serve 50 ml of soup A and 50 ml of soup B, and
Serve 25 ml of soup A and 75 ml of soup B.
When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: n = 50
Output: 0.62500
Explanation: If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
Example 2:

Input: n = 100
Output: 0.71875
 

Constraints:

0 <= n <= 109 */

/**
 * @param {number} n
 * @return {number}
 */
 var soupServings = function(n) {
    if(n>4800) return 1
    const NUM = 10
    let arr = new Array(NUM).fill(0).map(()=>new Array(NUM).fill(0))
    for(let i=0;i<NUM;i++){
        for(let j=0;j<NUM;j++){
            if(i==0&&j==0){
                arr[i][j] = 0.5
            }else if(i==0){
                arr[i][j] = 1
            }else if(j==0){
                arr[i][j] = 0
            }else{
                arr[i][j] = 0.25*(arr[Math.max(Math.ceil((i-100 / 25)),0)][j] + arr[Math.max(Math.ceil((i-75 / 25)),0)][Math.max(Math.ceil((j-25 / 25)),0)] + arr[Math.max(Math.ceil((i-50 / 25)),0)][Math.max(Math.ceil((j-50 / 25)),0)] + arr[Math.max(Math.ceil((i-25 / 25)),0)][Math.max(Math.ceil((j-75 / 25)),0)])
            }
        }
    }
    console.log(arr)
    return arr[Math.ceil(n/25)][Math.ceil(n/25)]

};

console.log(soupServings(100))