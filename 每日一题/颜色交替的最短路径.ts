/* 在一个有向图中，节点分别标记为 0, 1, ..., n-1。图中每条边为红色或者蓝色，且存在自环或平行边。

red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。

返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。

 

示例 1：

输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]
示例 2：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]
示例 3：

输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
输出：[0,-1,-1]
示例 4：

输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
输出：[0,1,2]
示例 5：

输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
输出：[0,1,1] */

function shortestAlternatingPaths(
    n: number,
    redEdges: number[][],
    blueEdges: number[][]
): number[] {
    // 构建邻接表
    const redEdgeMap: Map<number, number[]> = new Map();
    for (let edge of redEdges) {
        const [u, v] = edge;
        if (redEdgeMap.has(u)) {
            redEdgeMap.get(u)!.push(v);
        } else {
            redEdgeMap.set(u, [v]);
        }
        // 有向边
        /*         if (redEdgeMap.has(v)) {
            redEdgeMap.get(v).push(u)
        } else {
            redEdgeMap.set(v, [u])
        } */
    }
    const blueEdgeMap: Map<number, number[]> = new Map();
    for (let edge of blueEdges) {
        const [u, v] = edge;
        if (blueEdgeMap.has(u)) {
            blueEdgeMap.get(u)!.push(v);
        } else {
            blueEdgeMap.set(u, [v]);
        }
        /* if (blueEdgeMap.has(v)) {
            blueEdgeMap.get(v).push(u)
        } else {
            blueEdgeMap.set(v, [u])
        } */
    }

    // 首选红色
    let res = new Array(n).fill(0);

    function bfs(curN: number, nextColorIsBlue: boolean) {
        const searchedNodes = new Set<string>();
        let redLen = 0;
        const stack = [0];
        while (stack.length > 0) {
            let stackLen = stack.length;
            for (let i = 0; i < stackLen; i++) {
                const curNode = stack.shift() as number;
                if (curNode === curN) {
                    return redLen;
                }
                if (nextColorIsBlue) {
                    if (blueEdgeMap.has(curNode)) {
                        for (let node of blueEdgeMap.get(curNode)!) {
                            const key = `${curNode}-${node}-${nextColorIsBlue}`;
                            if (!searchedNodes.has(key)) {
                                stack.push(node);
                                searchedNodes.add(key);
                            }
                        }
                    }
                } else {
                    if (redEdgeMap.has(curNode)) {
                        for (let node of redEdgeMap.get(curNode)!) {
                            const key = `${curNode}-${node}-${nextColorIsBlue}`;
                            if (!searchedNodes.has(key)) {
                                stack.push(node);
                                searchedNodes.add(key);
                            }
                        }
                    }
                }
            }
            nextColorIsBlue = !nextColorIsBlue;
            redLen++;
        }
        return -1;
    }
    // console.log(redEdgeMap, blueEdgeMap)
    for (let i = 1; i < n; i++) {
        let redFirst = bfs(i, false);
        let blueFirst = bfs(i, true);
        // console.log(redFirst, blueFirst)
        if (redFirst === -1) {
            res[i] = blueFirst;
        } else if (blueFirst === -1) {
            res[i] = redFirst;
        } else {
            res[i] = Math.min(redFirst, blueFirst);
        }
    }
    return res;
}

console.log(shortestAlternatingPaths(5, [[2,0],[4,3],[4,4],[3,0],[1,4]], [[2,1],[4,3],[3,1],[3,0],[1,1],[2,0],[0,3],[3,3],[2,3]]))
console.log(shortestAlternatingPaths(3, [[0,1],[1,2]], []))
console.log(shortestAlternatingPaths(3, [[0,1]], [[2,1]]))
console.log(shortestAlternatingPaths(3, [[1,0]], [[2,1]]))
console.log(shortestAlternatingPaths(3, [[0,1]], [[1,2]]))
console.log(shortestAlternatingPaths(3, [[0,1],[0,2]], [[1,0]]))
console.log(shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]))