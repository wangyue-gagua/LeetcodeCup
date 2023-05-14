""" 推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。

游戏地图用大小为 m x n 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。

现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ：

玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
地板用字符 '.' 表示，意味着可以自由行走。
墙用字符 '#' 表示，意味着障碍物，不能通行。 
箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。
玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
玩家无法越过箱子。
返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。

 

示例 1：



输入：grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#",".","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：3
解释：我们只需要返回推箱子的次数。
示例 2：

输入：grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#","#","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：-1
示例 3：

输入：grid = [["#","#","#","#","#","#"],
             ["#","T",".",".","#","#"],
             ["#",".","#","B",".","#"],
             ["#",".",".",".",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：5
解释：向下、向左、向左、向上再向上。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid 仅包含字符 '.', '#',  'S' , 'T', 以及 'B'。
grid 中 'S', 'B' 和 'T' 各只能出现一个。 """

from typing import List


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        # 对箱子采用广度优先搜索判定最小推动次数
        # 箱子推动方向要求反方向是地板，并且人可以从当前位置移动到箱子的反方向所在位置
        m = len(grid)
        n = len(grid[0])

        # 实时更新grid
        def checkCanHumanReach(curPosX: int, curPosY: int, targetPosX: int,
                               targetPosY: int, curBoxPosX: int,
                               curBoxPosY: int):
            # 人能否到达目标位置
            # 深度优先搜索
            # print(grid)
            stack = []
            stack.append((curPosX, curPosY))
            visited = set()
            visited.add((curPosX, curPosY))
            while stack:
                curPosX, curPosY = stack.pop()
                if curPosX == targetPosX and curPosY == targetPosY:
                    return True
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nextPosX = curPosX + dx
                    nextPosY = curPosY + dy
                    if 0 <= nextPosX < m and 0 <= nextPosY < n and grid[
                            nextPosX][nextPosY] != '#' and (
                                nextPosX,
                                nextPosY) != (curBoxPosX, curBoxPosY) and (
                                    nextPosX, nextPosY) not in visited:
                        stack.append((nextPosX, nextPosY))
                        visited.add((nextPosX, nextPosY))
            return False

        # 遍历grid获取人、箱子、目标位置, 并清除已有人与箱子
        humanPos = (-1, -1)
        boxPos = (-1, -1)
        targetPos = (-1, -1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    humanPos = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == 'B':
                    boxPos = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == 'T':
                    targetPos = (i, j)

        # print(checkCanHumanReach(humanPos[0], humanPos[1], boxPos[0] + 1, boxPos[1], boxPos[0], boxPos[1]))
        # print(checkCanHumanReach(humanPos[0], humanPos[1], boxPos[0] - 1, boxPos[1], boxPos[0], boxPos[1]))
        # print(checkCanHumanReach(humanPos[0], humanPos[1], boxPos[0], boxPos[1] + 1, boxPos[0], boxPos[1]))
        # print(checkCanHumanReach(humanPos[0], humanPos[1], boxPos[0], boxPos[1] - 1, boxPos[0], boxPos[1]))

        # 回溯
        stack = []
        stack.append((boxPos[0], boxPos[1], humanPos[0], humanPos[1], 0))
        visited = set()
        visited.add((boxPos[0], boxPos[1], humanPos[0], humanPos[1]))
        while stack:
            curBoxPosX, curBoxPosY, curHumanPosX, curHumanPosY, curPushCount = stack.pop(0
            )
            if curBoxPosX == targetPos[0] and curBoxPosY == targetPos[1]:
                return curPushCount
            # 有可能没有完全围起来，还是要判断边界
            # 箱子左移
            ## 要求箱子左侧为地板
            if (0 <= curBoxPosX - 1 < m
                    and grid[curBoxPosX - 1][curBoxPosY] != '#'
                    and checkCanHumanReach(curHumanPosX, curHumanPosY,
                                           curBoxPosX + 1, curBoxPosY,
                                           curBoxPosX, curBoxPosY)):
                if (curBoxPosX - 1, curBoxPosY, curBoxPosX,
                        curBoxPosY) not in visited:
                    stack.append((curBoxPosX - 1, curBoxPosY, curBoxPosX,
                                  curBoxPosY, curPushCount + 1))
                    visited.add(
                        (curBoxPosX - 1, curBoxPosY, curBoxPosX, curBoxPosY))
            # 箱子右移
            ## 要求箱子右侧为地板
            if (0 <= curBoxPosX + 1 < m
                    and grid[curBoxPosX + 1][curBoxPosY] != '#'
                    and checkCanHumanReach(curHumanPosX, curHumanPosY,
                                           curBoxPosX - 1, curBoxPosY,
                                           curBoxPosX, curBoxPosY)):
                if (curBoxPosX + 1, curBoxPosY, curBoxPosX,
                        curBoxPosY) not in visited:
                    stack.append((curBoxPosX + 1, curBoxPosY, curBoxPosX,
                                  curBoxPosY, curPushCount + 1))
                    visited.add(
                        (curBoxPosX + 1, curBoxPosY, curBoxPosX, curBoxPosY))
            # 箱子上移
            ## 要求箱子上侧为地板
            if (0 <= curBoxPosY - 1 < n
                    and grid[curBoxPosX][curBoxPosY - 1] != '#'
                    and checkCanHumanReach(curHumanPosX, curHumanPosY,
                                           curBoxPosX, curBoxPosY + 1,
                                           curBoxPosX, curBoxPosY)):
                if (curBoxPosX, curBoxPosY - 1, curBoxPosX,
                        curBoxPosY) not in visited:
                    stack.append((curBoxPosX, curBoxPosY - 1, curBoxPosX,
                                  curBoxPosY, curPushCount + 1))
                    visited.add(
                        (curBoxPosX, curBoxPosY - 1, curBoxPosX, curBoxPosY))
            # 箱子下移
            ## 要求箱子下侧为地板
            if (0 <= curBoxPosY + 1 < n
                    and grid[curBoxPosX][curBoxPosY + 1] != '#'
                    and checkCanHumanReach(curHumanPosX, curHumanPosY,
                                           curBoxPosX, curBoxPosY - 1,
                                           curBoxPosX, curBoxPosY)):
                if (curBoxPosX, curBoxPosY + 1, curBoxPosX,
                        curBoxPosY) not in visited:
                    stack.append((curBoxPosX, curBoxPosY + 1, curBoxPosX,
                                  curBoxPosY, curPushCount + 1))
                    visited.add(
                        (curBoxPosX, curBoxPosY + 1, curBoxPosX, curBoxPosY))
        return -1


testGird = [["#", "#", "#", "#", "#", "#"], ["#", "T", "#", "#", "#", "#"],
            ["#", ".", ".", "B", ".", "#"], ["#", ".", "#", "#", ".", "#"],
            ["#", ".", ".", ".", "S", "#"], ["#", "#", "#", "#", "#", "#"]]

print(Solution().minPushBox(testGird))