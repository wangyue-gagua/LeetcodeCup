/* 给你一个整数数组 nums ，返回其中 按位与三元组 的数目。

按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：

0 <= i < nums.length
0 <= j < nums.length
0 <= k < nums.length
nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。
 
示例 1：

输入：nums = [2,1,3]
输出：12
解释：可以选出如下 i, j, k 三元组：
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2 */

function countTriplets(nums: number[]): number {
    // 统计每个数字出现的次数
    const count = new Map<number, number>();
    for (const num of nums) {
        count.set(num, (count.get(num) || 0) + 1);
    }
    // 暴力求解数字组合的可能性
    const allUniqNums = [...count.keys()];

    let ans = 0;
    // 3个同样的数字 要求全为0
    const zeroCnt = count.get(0) || 0;
    if (zeroCnt >= 3) {
        ans += (zeroCnt * (zeroCnt - 1) * (zeroCnt - 2) / 6) * 27;
    }

    // 一个0
    if (zeroCnt === 1) {
        ans += 1
    }

    // 2个同样的数字 加上一个不同的数字， 相当于 2个不同的数字的按位与
    for (let i = 0; i < allUniqNums.length; i++) {
        for (let j = i + 1; j < allUniqNums.length; j++) {
            const num = allUniqNums[i] & allUniqNums[j];
            if (num === 0) {
                const counti = count.get(allUniqNums[i])!;
                const countj = count.get(allUniqNums[j])!;

                if (counti > 1 && countj === 1) {
                    ans += counti * (counti - 1)  * 3 * countj;
                } else if (counti === 1 && countj > 1) {
                    ans += countj * (countj - 1) * 3 * counti;
                } else if (counti > 1 && countj > 1) {
                    ans += (counti * (counti - 1)  * 3 * countj) + (countj * (countj - 1) * 3 * counti);
                } else {
                    continue
                }
            }
        }
    }

    // 需要考虑取同一个坐标2次的情况
    // 2个同样的数字 加上一个不同的数字， 相当于 2个不同的数字的按位与
    for (let i = 0; i < allUniqNums.length; i++) {
        for (let j = i + 1; j < allUniqNums.length; j++) {
            const num = allUniqNums[i] & allUniqNums[j];
            if (num === 0) {
                const counti = count.get(allUniqNums[i])!;
                const countj = count.get(allUniqNums[j])!;
                ans += counti * countj * 6;
            }
        }
    }

    // 3个不同的数字
    for (let i = 0; i < allUniqNums.length; i++) {
        for (let j = i + 1; j < allUniqNums.length; j++) {
            for (let k = j + 1; k < allUniqNums.length; k++) {
                if ((allUniqNums[i] & allUniqNums[j] & allUniqNums[k]) === 0) {
                    const counti = count.get(allUniqNums[i])!;
                    const countj = count.get(allUniqNums[j])!;
                    const countk = count.get(allUniqNums[k])!;

                    ans += counti * countj * countk * 6;
                }
            }
        }
    }

    return ans;
};

console.log(countTriplets([2,1,3]));
console.log(countTriplets([0,0,0]));