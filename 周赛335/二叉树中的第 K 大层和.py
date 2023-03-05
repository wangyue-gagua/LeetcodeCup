""" 给你一棵二叉树的根节点 root 和一个正整数 k 。

树中的 层和 是指 同一层 上节点值的总和。

返回树中第 k 大的层和（不一定不同）。如果树少于 k 层，则返回 -1 。

注意，如果两个节点与根节点的距离相同，则认为它们在同一层。

 输入：root = [5,8,9,2,1,3,7,4,6], k = 2
输出：13
解释：树中每一层的层和分别是：
- Level 1: 5
- Level 2: 8 + 9 = 17
- Level 3: 2 + 1 + 3 + 7 = 13
- Level 4: 4 + 6 = 10
第 2 大的层和等于 13 。

输入：root = [1,2,null,3], k = 1
输出：3
解释：最大的层和是 3 。
  """

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        queue = [root]
        level = 0
        level_sum = []
        while queue:
            level += 1
            level_sum.append(0)
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_sum[level - 1] += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        if k > level:
            return -1
        else:
            return sorted(level_sum, reverse=True)[k - 1]
        
        

