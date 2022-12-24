""" 给你一个顾客访问商店的日志，用一个下标从 0 开始且只包含字符 'N' 和 'Y' 的字符串 customers 表示：

如果第 i 个字符是 'Y' ，它表示第 i 小时有顾客到达。
如果第 i 个字符是 'N' ，它表示第 i 小时没有顾客到达。
如果商店在第 j 小时关门（0 <= j <= n），代价按如下方式计算：

在开门期间，如果某一个小时没有顾客到达，代价增加 1 。
在关门期间，如果某一个小时有顾客到达，代价增加 1 。
请你返回在确保代价 最小 的前提下，商店的 最早 关门时间。

注意，商店在第 j 小时关门表示在第 j 小时以及之后商店处于关门状态。

 

示例 1：

输入：customers = "YYNY"
输出：2
解释：
- 第 0 小时关门，总共 1+1+0+1 = 3 代价。
- 第 1 小时关门，总共 0+1+0+1 = 2 代价。
- 第 2 小时关门，总共 0+0+0+1 = 1 代价。
- 第 3 小时关门，总共 0+0+1+1 = 2 代价。
- 第 4 小时关门，总共 0+0+1+0 = 1 代价。
在第 2 或第 4 小时关门代价都最小。由于第 2 小时更早，所以最优关门时间是 2 。
示例 2：

输入：customers = "NNNNN"
输出：0
解释：最优关门时间是 0 ，因为自始至终没有顾客到达。
示例 3：

输入：customers = "YYYY"
输出：4
解释：最优关门时间是 4 ，因为每一小时均有顾客到达。
 

提示：

1 <= customers.length <= 105
customers 只包含字符 'Y' 和 'N' 。 """

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        if n == 1:
            return 1 if customers[0] == 'Y' else 0
        dp = [[0] * 2 for _ in range(n + 1)]
        # dp[i][0] 表示前i个字符的N的数量 dp[i][1] 表示后n - i个字符的Y的数量
        dp[0][1] = customers.count('Y')
        minVal = dp[0][1]
        minValIndex = 0
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + (1 if customers[i - 1] == 'N' else 0)
            dp[i][1] = dp[i - 1][1] - (1 if customers[i - 1] == 'Y' else 0)
            if dp[i][0] + dp[i][1] < minVal:
                minVal = dp[i][0] + dp[i][1]
                minValIndex = i
        # print(dp)
        return minValIndex


print(Solution().bestClosingTime("YYYY"))