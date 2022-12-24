/* We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X. */

/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number[]} profit
 * @return {number}
 */
 var jobScheduling = function(startTime, endTime, profit) {
    // 区间问题
    // 1. 按照结束时间排序
    // 2. dp[i] = max(dp[i-1], dp[j] + profit[i])
    // 3. j = 0 ~ i-1
    // 4. endTime[j] <= startTime[i]
    let n = startTime.length;
    let jobs = [];
    for (let i = 0; i < n; i++) {
        jobs.push([startTime[i], endTime[i], profit[i]]);
    }
    jobs.sort((a, b) => a[1] - b[1]);
    let dp = new Array(n + 1).fill(0);
    console.log(jobs);
    const binarySearch = (jobs, right, target) => {
        let left = 0;
        while (left < right) {
            const mid = left + Math.floor((right - left) / 2);
            if (jobs[mid][1] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    };
    for (let i = 1; i <=n; i++) {
        const k = binarySearch(jobs, i, jobs[i - 1][0]);
        dp[i] = Math.max(dp[i - 1], dp[k] + jobs[i - 1][2]);
    }
    return dp[n];
};

console.log(jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]));
