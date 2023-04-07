""" 在一个长度 无限 的数轴上，第 i 颗石子的位置为 stones[i]。如果一颗石子的位置最小/最大，那么该石子被称作 端点石子 。

每个回合，你可以将一颗端点石子拿起并移动到一个未占用的位置，使得该石子不再是一颗端点石子。

值得注意的是，如果石子像 stones = [1,2,5] 这样，你将 无法 移动位于位置 5 的端点石子，因为无论将它移动到任何位置（例如 0 或 3），该石子都仍然会是端点石子。

当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。

要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves] 。

 

示例 1：

输入：[7,4,9]
输出：[1,2]
解释：
我们可以移动一次，4 -> 8，游戏结束。
或者，我们可以移动两次 9 -> 5，4 -> 6，游戏结束。
示例 2：

输入：[6,5,4,3,10]
输出：[2,3]
解释：
我们可以移动 3 -> 8，接着是 10 -> 7，游戏结束。
或者，我们可以移动 3 -> 7, 4 -> 8, 5 -> 9，游戏结束。
注意，我们无法进行 10 -> 2 这样的移动来结束游戏，因为这是不合要求的移动。
示例 3：

输入：[100,101,104,102,103]
输出：[0,0]
 

提示：

3 <= stones.length <= 10^4
1 <= stones[i] <= 10^9
stones[i] 的值各不相同。 """

from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        max_gap = max(stones[i + 1] - stones[i] - 1 for i in range(n - 1))
        min_gap = min(stones[n - 1] - stones[1] - n + 2,
                      stones[n - 2] - stones[0] - n + 2)
        for i in range(n - 1):
            if stones[i + 1] - stones[i] + 1 == n - 1 and stones[
                    i + 1] - stones[0] + 1 > n - 1:
                min_gap = min(min_gap, 2)
        return [min_gap, max_gap]


def numMovesStones(stones: List[int]):
    # 先对数组进行排序
    stones.sort()
    lens = len(stones)
    # 遍历stones获取空缺位置
    gaps = []
    for i in range(lens - 1):
        gap = stones[i + 1] - stones[i] - 1
        if gap > 0:
            for j in range(stones[i] + 1, stones[i + 1]):
                gaps.append(j)
    # 计算最小步数
    ## 左端点右边可用间隔为 stones[-1] - stones[1] + 2 - lens
    ## 右端点左边可用间隔为 stones[-2] - stones[0] + 2 - lens
    min_step = lens
    while True:
        rightGap = stones[-1] - stones[1] + 2 - lens
        leftGap = stones[-2] - stones[0] + 2 - lens
        if rightGap == 0 and leftGap == 0:
            break
        elif rightGap <= leftGap:
            # 左端点右移
            


# print(Solution().numMovesStonesII([7,4,9]))
# print(Solution().numMovesStonesII([6,5,4,3,10]))

print(numMovesStones([7, 4, 9]))
print(numMovesStones([6, 5, 4, 3, 10]))
