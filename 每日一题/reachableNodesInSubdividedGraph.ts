/* You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1. You decide to subdivide each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates that there is an edge between nodes ui and vi in the original graph, and cnti is the total number of new nodes that you will subdivide the edge into. Note that cnti == 0 means you will not subdivide the edge.

To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes. The new nodes are x1, x2, ..., xcnti, and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [xcnti-1, xcnti], [xcnti, vi].

In this new graph, you want to know how many nodes are reachable from the node 0, where a node is reachable if the distance is maxMoves or less.

Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.

 

Example 1:


Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
Output: 13
Explanation: The edge subdivisions are shown in the image above.
The nodes that are reachable are highlighted in yellow.
Example 2:

Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
Output: 23
Example 3:

Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
Output: 1
Explanation: Node 0 is disconnected from the rest of the graph, so only node 0 is reachable. */

function reachableNodes(edges: number[][], maxMoves: number, n: number): number {
    const graph = new Map();
    for (let i = 0; i < n; i++) {
        graph.set(i, new Map());
    }
    for (const [u, v, w] of edges) {
        graph.get(u).set(v, w);
        graph.get(v).set(u, w);
    }
    const pq = new PriorityQueue<number[]>((a: number[], b: number[]) => b[0] - a[0]);
    pq.push([maxMoves, 0]);
    const seen = new Map();
    seen.set(0, maxMoves);
    let ans = 0;
    while (pq.size()) {
        const [moves, i] = pq.pop();
        ans++;
        for (const [j, w] of graph.get(i).entries()) {
            const moves2 = moves - w - 1;
            if (moves2 >= 0 && (!seen.has(j) || moves2 > seen.get(j))) {
                seen.set(j, moves2);
                pq.push([moves2, j]);
            }
            ans += Math.min(moves, w);
        }
    }
    for (const [u, v, w] of edges) {
        ans += Math.min(seen.get(u) || 0, w) + Math.min(seen.get(v) || 0, w);
    }
    return ans;
};

class PriorityQueue<T> {
    private heap: T[];
    private compare: (a: T, b: T) => number;
    constructor(compare: (a: T, b: T) => number) {
        this.heap = [];
        this.compare = compare;
    }
    size() {
        return this.heap.length;
    }
    push(val: T) {
        this.heap.push(val);
        this._siftUp();
    }
    pop() {
        const top = this.heap[0];
        const bottom = this.heap.pop() as T;
        if (this.heap.length > 0) {
            this.heap[0] = bottom;
            this._siftDown();
        }
        return top;
    }
    peek() {
        return this.heap[0];
    }
    _parent(i: number) {
        return ((i + 1) >>> 1) - 1;
    }
    _left(i: number) {
        return (i << 1) + 1;
    }
    _right(i: number) {
        return (i + 1) << 1;
    }
    _greater(i: number, j: number) {
        return this.compare(this.heap[i], this.heap[j]) > 0;
    }
    _siftUp() {
        let node = this.heap.length - 1;
        while (node > 0 && this._greater(node, this._parent(node))) {
            const parent = this._parent(node);
            [this.heap[parent], this.heap[node]] = [this.heap[node], this.heap[parent]];
            node = parent;
        }
    }
    _siftDown() {
        let node = 0;
        while (
            (this._left(node) < this.heap.length && this._greater(this._left(node), node)) ||
            (this._right(node) < this.heap.length && this._greater(this._right(node), node))
        ) {
            let maxChild = (this._right(node) < this.heap.length && this._greater(this._right(node), this._left(node))) ? this._right(node) : this._left(node);
            [this.heap[node], this.heap[maxChild]] = [this.heap[maxChild], this.heap[node]];
            node = maxChild;
        }
    }
}

console.log(reachableNodes([[0,1,10],[0,2,1],[1,2,2]], 6, 3));