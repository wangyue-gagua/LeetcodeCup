""" 你还记得那条风靡全球的贪吃蛇吗？

我们在一个 n*n 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（(0, 0) 和 (0, 1)）开始移动。我们用 0 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（(n-1, n-2) 和 (n-1, n-1)）。

每次移动，蛇可以这样走：

如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（(r, c)、(r, c+1)）移动到 （(r, c)、(r+1, c)）。

如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（(r, c)、(r+1, c)）移动到（(r, c)、(r, c+1)）。

返回蛇抵达目的地所需的最少移动次数。

如果无法到达目的地，请返回 -1。

 

示例 1：



输入：grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
输出：11
解释：
一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。
示例 2：

输入：grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
输出：9 """

from typing import List, Tuple


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # dfs stack中保存的是当前的位置和方向
        # 0表示水平，1表示竖直
        # 初始值为(0, 1, 0) 终点为(n-1, n-1, 0)
        stack: List[Tuple[int, int, int]] = [(0, 1, 0)]
        n = len(grid)
        visited = set()
        visited.add((0, 1, 0))

        step = 0
        while stack:
            for _ in range(len(stack)):
                x, y, d = stack.pop(0)
                if x == n - 1 and y == n - 1 and d == 0:
                    return step
                # 向右走
                # 如果是水平状态，向右走一步
                if d == 0 and y + 1 < n and grid[x][y + 1] == 0:
                    if (x, y + 1, d) not in visited:
                        stack.append((x, y + 1, d))
                        visited.add((x, y + 1, d))
                # 如果是竖直状态，竖直向右移动
                if d == 1 and y + 1 < n and grid[x][y + 1] == 0 and grid[x - 1][
                        y + 1] == 0:
                    if (x, y + 1, d) not in visited:
                        stack.append((x, y + 1, d))
                        visited.add((x, y + 1, d))
                # 向下走
                # 如果是水平状态，水平向下移动
                if d == 0 and x + 1 < n and grid[x + 1][y] == 0 and grid[x + 1][
                        y - 1] == 0:
                    if (x + 1, y, d) not in visited:
                        stack.append((x + 1, y, d))
                        visited.add((x + 1, y, d))
                # 如果是竖直状态，向下走一步
                if d == 1 and x + 1 < n and grid[x + 1][y] == 0:
                    if (x + 1, y, d) not in visited:
                        stack.append((x + 1, y, d))
                        visited.add((x + 1, y, d))
                # 顺时针旋转
                if d == 0 and x + 1 < n and grid[x + 1][y] == 0 and grid[x + 1][
                        y - 1] == 0:
                    if (x + 1, y - 1, 1) not in visited:
                        stack.append((x + 1, y - 1, 1))
                        visited.add((x + 1, y - 1, 1))
                # 逆时针旋转
                if d == 1 and y + 1 < n and grid[x][y + 1] == 0 and grid[x - 1][
                        y + 1] == 0:
                    if (x - 1, y + 1, 0) not in visited:
                        stack.append((x - 1, y + 1, 0))
                        visited.add((x - 1, y + 1, 0))
            step += 1
        return -1


arr = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
print(Solution().minimumMoves((arr)))