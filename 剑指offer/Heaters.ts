/* Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.

 

Example 1:

Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
Example 3:

Input: houses = [1,5], heaters = [2]
Output: 3 */

function findRadius(houses: number[], heaters: number[]): number {
    // 二分法
    houses.sort((a, b) => a - b);
    heaters.sort((a, b) => a - b);
    let res = 0;
    for (const house of houses) {
        let left = 0, right = heaters.length - 1;
        while (left < right) {
            const mid = left + Math.floor((right - left) / 2);
            if (heaters[mid] < house) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        const dist1 = Math.abs(heaters[left] - house);
        const dist2 = left > 0 ? Math.abs(heaters[left - 1] - house) : Infinity;
        res = Math.max(res, Math.min(dist1, dist2));
    }
    return res;
}

console.log(findRadius([1, 2, 3], [2]));
console.log(findRadius([1, 2, 3, 4], [1, 4]));
console.log(findRadius([1, 5], [2]));
console.log(findRadius([1, 5], [10]));
console.log(findRadius([1,2,3], [1,2,3]));
console.log(findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923], [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]));