""" 给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。

请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ：

mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。
maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。
返回数组 answer 。

 

示例 1 ：



输入：root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
输出：[[2,2],[4,6],[15,-1]]
解释：按下面的描述找出并返回查询的答案：
- 树中小于等于 2 的最大值是 2 ，且大于等于 2 的最小值也是 2 。所以第一个查询的答案是 [2,2] 。
- 树中小于等于 5 的最大值是 4 ，且大于等于 5 的最小值是 6 。所以第二个查询的答案是 [4,6] 。
- 树中小于等于 16 的最大值是 15 ，且大于等于 16 的最小值不存在。所以第三个查询的答案是 [15,-1] 。
示例 2 ：



输入：root = [4,null,9], queries = [3]
输出：[[-1,4]]
解释：树中不存在小于等于 3 的最大值，且大于等于 3 的最小值是 4 。所以查询的答案是 [-1,4] 。 

示例 3：
输入：root = [16,8,18,1,12,null,20,null,2,9,null,null,null,null,7], queries = [8,14,285508,6]
输出：[[8,8],[12,16],[20,-1],[2,7]]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import bisect
from typing import List, Optional


class Solution:
    def closestNodes(self, root: Optional[TreeNode],
                     queries: List[int]) -> List[List[int]]:
                     
        # 二叉搜索树的中序遍历是有序的
        NodeList = []
        def inorder(root: Optional[TreeNode]):
            if not root:
                return
            inorder(root.left)
            NodeList.append(root.val)
            inorder(root.right)
        # print(NodeList)
        inorder(root)
        ans = []
        for q in queries:
            index = bisect.bisect_left(NodeList, q)
            if index == len(NodeList):
                ans.append([NodeList[-1], -1])
            elif index == 0 and NodeList[0] > q:
                ans.append([-1, NodeList[0]])
            elif NodeList[index] == q:
                ans.append([q, q])
            else:
                ans.append([NodeList[index - 1], NodeList[index]])
        return ans



Tree = TreeNode(16, TreeNode(8, TreeNode(1, None, TreeNode(2, None, TreeNode(7))), TreeNode(12, TreeNode(9))), TreeNode(18, None, TreeNode(20)))

# 层次遍历打印二叉树
def levelPrintTree(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            queue.append(node.left)
            queue.append(node.right)
            print(node.val, end=' ')
        else:
            print('null', end=' ')
        

levelPrintTree(Tree)




# 示例3
print(Solution().closestNodes(Tree, [8, 14, 285508, 6]))
