/* 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。

我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。

所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。

请你返回「表现良好时间段」的最大长度。

 

示例 1：

输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]。
示例 2：

输入：hours = [6,6,6]
输出：0
 

提示：

1 <= hours.length <= 104
0 <= hours[i] <= 16 */

function longestWPI(hours: number[]): number {
    // 先试试暴力法
    function ぼうりょく() {
        let windowSize = 1;
        const days = hours.length;
        // 计算前缀和
        const prefixSum = new Array(days + 1).fill(0);
        let max = 0;
        for (let i = 1; i <= days; i++) {
            prefixSum[i] = prefixSum[i - 1] + (hours[i - 1] > 8 ? 1 : -1);
        }
        while (windowSize <= days) {
            let hasFound = false;
            for (let i = windowSize; i <= days; i++) {
                // 在windowSize范围内，计算前缀和
                const tiringDays = prefixSum[i] - prefixSum[i - windowSize];
                if (tiringDays > 0) {
                    max = Math.max(max, windowSize);
                    // hasFound = true
                    break;
                }
            }
            // if (!hasFound) {
            //     break
            // }
            windowSize++;
        }
        return max;
    }

    // 哈希表存储s[j] = s[i] - 1
    function 哈希表() {
        const days = hours.length;
        // 计算前缀和
        const prefixSum = new Array(days + 1).fill(0);
        let max = 0;
        const map = new Map();
        for (let i = 1; i <= days; i++) {
            prefixSum[i] = prefixSum[i - 1] + (hours[i - 1] > 8 ? 1 : -1);
            if (prefixSum[i] > 0) {
                max = i;
            } else {
                if (!map.has(prefixSum[i])) {
                    map.set(prefixSum[i], i);
                }
                if (map.has(prefixSum[i] - 1)) {
                    max = Math.max(max, i - map.get(prefixSum[i] - 1));
                }
            }
        }
        return max;
    }


    return 哈希表();
}

console.log(longestWPI([9, 9, 6, 0, 6, 6, 9]));
console.log(longestWPI([6, 6, 6]));
console.log(longestWPI([9, 6, 9]));
