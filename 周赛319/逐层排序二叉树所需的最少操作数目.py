""" 给你一个 值互不相同 的二叉树的根节点 root 。

在一步操作中，你可以选择 同一层 上任意两个节点，交换这两个节点的值。

返回每一层按 严格递增顺序 排序所需的最少操作数目。

节点的 层数 是该节点和根节点之间的路径的边数。

 

示例 1 ：


输入：root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
输出：3
解释：
- 交换 4 和 3 。第 2 层变为 [3,4] 。
- 交换 7 和 5 。第 3 层变为 [5,6,8,7] 。
- 交换 8 和 7 。第 3 层变为 [5,6,7,8] 。
共计用了 3 步操作，所以返回 3 。
可以证明 3 是需要的最少操作数目。
示例 2 ：


输入：root = [1,3,2,7,6,5,4]
输出：3
解释：
- 交换 3 和 2 。第 2 层变为 [2,3] 。 
- 交换 7 和 4 。第 3 层变为 [4,6,5,7] 。 
- 交换 6 和 5 。第 3 层变为 [4,5,6,7] 。
共计用了 3 步操作，所以返回 3 。 
可以证明 3 是需要的最少操作数目。
示例 3 ：


输入：root = [1,2,3,4,5,6]
输出：0
解释：每一层已经按递增顺序排序，所以返回 0 。 """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import math
from typing import List, Optional


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # 层次遍历
        # 逐层排序

        def exChangeSortNum(nums: List[int]) -> int:
            """返回两两交换使得数组有序的最小交换次数, 交换环"""
            # Nnode = len(nums)
            # Nring
            # res = Nnode - Nring

            posMap = {}
            sorted_nums = sorted(nums)
            for i in range(len(sorted_nums)):
                posMap[sorted_nums[i]] = i

            res = 0
            searched = [False] * len(nums)
            for i in range(len(nums)):
                if searched[i]:
                    continue
                j = i
                while not searched[j]:
                    searched[j] = True
                    j = posMap[nums[j]]
                res += 1
            return len(nums) - res
        # 如果树回退到链表，则返回0
        # 判断是否为链表
        if root.left and root.right is None and root.left.left and root.left.right is None and root.left.left.left and root.left.left.right is None:
            return 0

        res = 0
        queue: List[Optional[TreeNode]] = [root]
        while queue:
            layerNode = []
            for i in range(len(queue)):
                node = queue.pop(0)
                layerNode.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += exChangeSortNum(layerNode)
        return res
