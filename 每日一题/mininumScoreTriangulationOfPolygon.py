""" /* You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex (i.e., clockwise order).

You will triangulate the polygon into n - 2 triangles. For each triangle, the value of that triangle is the product of the values of its vertices, and the total score of the triangulation is the sum of these values over all n - 2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

 

Example 1:


Input: values = [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
Example 2:


Input: values = [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.
Example 3:


Input: values = [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
 

Constraints:

n == values.length
3 <= n <= 50
1 <= values[i] <= 100 */ """

from functools import lru_cache
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dfs(path: str):
            """返回以arr为所有顶点构成的三角剖分的最小值"""
            arr = [int(i) for i in path.split(',')]
            lens = len(arr)
            if lens == 3:
                return arr[0] * arr[1] * arr[2]
            else:
                ans = 10000000
                # 以values[n]为顶点构成的三角剖分为
                for i in range(lens):
                    # 当前顶点为arr[i]，左右两边的顶点为arr[(i - 1 + lens) % lens]和arr[(i+1) % lens])]
                    curVal = arr[(i - 1 + lens) %
                                 lens] * arr[i] * arr[(i + 1) % lens]
                    # 递归求解
                    newArr = arr[:i] + arr[i + 1:]
                    ans = min(ans,
                              curVal + dfs(','.join([str(i) for i in newArr])))
                return ans

        return dfs(",".join([str(i) for i in values]))
    
    def memorySearch(self, values: List[int]) -> int:
        """动态规划"""
        n = len(values)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = min([dp[i][k] + dp[k][j] + values[i] * values[k] * values[j] for k in range(i + 1, j)])
        return dp[0][n - 1]


print(Solution().minScoreTriangulation([1, 2, 3]))
print(Solution().minScoreTriangulation([3, 7, 4, 5]))
print(Solution().minScoreTriangulation([1, 3, 1, 4, 1, 5]))
print(Solution().minScoreTriangulation([69,22,21,27,26,62,69,81,55,85,95,40,91,33,72,88,86])) 
print(Solution().memorySearch([35,73,90,27,71,80,21,33,33,13,48,12,68,70,80,36,66,3,70,58]))