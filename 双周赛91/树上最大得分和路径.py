""" 一个 n 个节点的无向树，节点编号为 0 到 n - 1 ，树的根结点是 0 号节点。给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] ，表示节点 ai 和 bi 在树中有一条边。

在每一个节点 i 处有一扇门。同时给你一个都是偶数的数组 amount ，其中 amount[i] 表示：

如果 amount[i] 的值是负数，那么它表示打开节点 i 处门扣除的分数。
如果 amount[i] 的值是正数，那么它表示打开节点 i 处门加上的分数。
游戏按照如下规则进行：

一开始，Alice 在节点 0 处，Bob 在节点 bob 处。
每一秒钟，Alice 和 Bob 分别 移动到相邻的节点。Alice 朝着某个 叶子结点 移动，Bob 朝着节点 0 移动。
对于他们之间路径上的 每一个 节点，Alice 和 Bob 要么打开门并扣分，要么打开门并加分。注意：
如果门 已经打开 （被另一个人打开），不会有额外加分也不会扣分。
如果 Alice 和 Bob 同时 到达一个节点，他们会共享这个节点的加分或者扣分。换言之，如果打开这扇门扣 c 分，那么 Alice 和 Bob 分别扣 c / 2 分。如果这扇门的加分为 c ，那么他们分别加 c / 2 分。
如果 Alice 到达了一个叶子结点，她会停止移动。类似的，如果 Bob 到达了节点 0 ，他也会停止移动。注意这些事件互相 独立 ，不会影响另一方移动。
请你返回 Alice 朝最优叶子结点移动的 最大 净得分。

 

示例 1：



输入：edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
输出：6
解释：
上图展示了输入给出的一棵树。游戏进行如下：
- Alice 一开始在节点 0 处，Bob 在节点 3 处。他们分别打开所在节点的门。
  Alice 得分为 -2 。
- Alice 和 Bob 都移动到节点 1 。
  因为他们同时到达这个节点，他们一起打开门并平分得分。
  Alice 的得分变为 -2 + (4 / 2) = 0 。
- Alice 移动到节点 3 。因为 Bob 已经打开了这扇门，Alice 得分不变。
  Bob 移动到节点 0 ，并停止移动。
- Alice 移动到节点 4 并打开这个节点的门，她得分变为 0 + 6 = 6 。
现在，Alice 和 Bob 都不能进行任何移动了，所以游戏结束。
Alice 无法得到更高分数。
示例 2：



输入：edges = [[0,1]], bob = 1, amount = [-7280,2350]
输出：-7280
解释：
Alice 按照路径 0->1 移动，同时 Bob 按照路径 1->0 移动。
所以 Alice 只打开节点 0 处的门，她的得分为 -7280 。 
"""

from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int,
                           amount: List[int]) -> int:
        """
        1. 从节点0开始，每次移动到相邻的节点，直到到达叶子节点或者节点0
        2. 每次移动，Alice和Bob都会打开这个节点的门，如果门已经打开，不会有额外加分也不会扣分
        3. 如果Alice和Bob同时到达一个节点，他们会共享这个节点的加分或者扣分，如果打开这扇门扣c分，那么Alice和Bob分别扣c/2分
        4. 如果这扇门的加分为c，那么他们分别加c/2分
        5. 如果Alice到达了一个叶子节点，她会停止移动，类似的，如果Bob到达了节点0，他也会停止移动
        6. 请你返回Alice朝最优叶子节点移动的最大净得分
        """
        # 1. 构建邻接表
        n = len(amount)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)

        # 2. 从节点0开始，每次移动到相邻的节点，直到到达叶子节点或者节点0
        # 3. 每次移动，Alice和Bob都会打开这个节点的门，如果门已经打开，不会有额外加分也不会扣分
        # 4. 如果Alice和Bob同时到达一个节点，他们会共享这个节点的加分或者扣分，如果打开这扇门扣c分，那么Alice和Bob分别扣c/2分
        # 5. 如果这扇门的加分为c，那么他们分别加c/2分
        # 6. 如果Alice到达了一个叶子节点，她会停止移动，类似的，如果Bob到达了节点0，他也会停止移动
        # 7. 请你返回Alice朝最优叶子节点移动的最大净得分

        # Alice从根节点dfs, Bob从叶子节点dfs
        isAliceBobSearched = [[False, False] for _ in range(n)]
        aliceScore = []
        BobPath: List[int] = []

        # 搜索Bob到达节点0的路径， 输出节点id
        def dfsBobPath(node, path, BobPath):
            if node == 0:
                BobPath.extend(path)
                return
            for child in graph[node]:
                if child not in path:
                    path.append(child)
                    dfsBobPath(child, path, BobPath)
                    path.pop()

        dfsBobPath(bob, [bob], BobPath)
        # print(BobPath)

        def dfs(aliceCur, BobCur, aliceCurScore, path):
            # print(aliceCur)

            BobCurNode = BobPath[BobCur]
            path.append(aliceCur)
            if aliceCur == BobCurNode:
                # 平分分数
                aliceCurScore += amount[aliceCur] / 2
            else:
                # Bob没有搜索过这个点
                if not isAliceBobSearched[aliceCur][
                        1] and not isAliceBobSearched[aliceCur][0]:
                    aliceCurScore += amount[aliceCur]
                # Bob搜索过这个点
                else:
                    aliceCurScore += 0
            isAliceBobSearched[aliceCur][0] = True
            BobCurNode = BobPath[BobCur]
            print(BobCurNode)
            isAliceBobSearched[BobCurNode][1] = True

            # 如果是叶子节点，直接返回
            if aliceCur != 0 and len(graph[aliceCur]) == 1:
                aliceScore.append(aliceCurScore)
                return
            # 如果不是叶子节点，继续搜索
            for nextNode in graph[aliceCur]:
                if nextNode not in path:
                    if BobCurNode == 0:
                        # print(aliceCur, graph[aliceCur])
                        dfs(nextNode, len(BobPath) - 1, aliceCurScore, path)
                        isAliceBobSearched[aliceCur][0] = False
                        isAliceBobSearched[BobCurNode][1] = False
                    else:
                        dfs(nextNode, BobCur + 1, aliceCurScore, path)
                        isAliceBobSearched[aliceCur][0] = False
                        isAliceBobSearched[BobCurNode][1] = False

        dfs(0, 0, 0, [])
        print(aliceScore)
        return int(max(aliceScore))


print(Solution().mostProfitablePath([[0,1],[0,2]], bob = 2, amount = [-3360,-5394,-1146]))
