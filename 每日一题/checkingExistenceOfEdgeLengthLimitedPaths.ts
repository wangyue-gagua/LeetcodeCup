/* An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

 

Example 1:


Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
Example 2:


Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph. */

class UnionFind {
    capital: number[];
    constructor(isConnected: number) {
        this.capital = new Array<number>(isConnected).fill(0);
        for (let i = 0; i < isConnected; i++) {
            this.capital[i] = i;
        }
    }

    union(i: number, j: number) {
        let iCapital = this.find(i);
        let jCapital = this.find(j);
        if (iCapital !== jCapital) {
            this.capital[jCapital] = iCapital;
        }
    }

    find(i: number): number {
        if (this.capital[i] === i) {
            return i;
        }
        return this.find(this.capital[i]);
    }
}

function distanceLimitedPathsExist(n: number, edgeList: number[][], queries: number[][]): boolean[] {
    const res = new Array(queries.length).fill(false);
    const sortedQueries = queries.map((q, i) => [q[2], q[0], q[1], i]).sort((a, b) => a[0] - b[0]);
    const sortedEdges = edgeList.sort((a, b) => a[2] - b[2]);
    const uf = new UnionFind(n);
    // console.log(uf.capital);
    let edgeIdx = 0;
    for (const [limit, p, q, i] of sortedQueries) {
        while (edgeIdx < sortedEdges.length && sortedEdges[edgeIdx][2] < limit) {
            uf.union(sortedEdges[edgeIdx][0], sortedEdges[edgeIdx][1]);
            edgeIdx++;
            // console.log(uf.capital);
        }
        res[i] = uf.find(p) === uf.find(q);
    }
    return res;

};


console.log(distanceLimitedPathsExist(4, [[0,1,1],[2,3,1]],  [[0,1,2],[0,2,1],[0,3,1],[1,2,1],[1,3,1],[2,3,1]]));

