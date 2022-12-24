# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import List, Optional, Set


class Solution:
    def treeQueries(self, root: Optional[TreeNode],
                    queries: List[int]) -> List[int]:
        dp = {}
        lmx = 0

        def defl(root: Optional[TreeNode], count):
            nonlocal lmx
            if not root:
                return
            dp[root.val] = lmx
            lmx = max(lmx, count)
            defl(root.left, count + 1)
            defl(root.right, count + 1)

        rmx = 0

        def defr(root: Optional[TreeNode], count):
            nonlocal rmx
            if not root:
                return
            dp[root.val] = max(dp[root.val], rmx)
            rmx = max(rmx, count)
            defr(root.right, count + 1)
            defr(root.left, count + 1)

        defl(root, 0)
        defr(root, 0)
        ans = []
        for i in queries:
            ans.append(dp[i])
        return ans
