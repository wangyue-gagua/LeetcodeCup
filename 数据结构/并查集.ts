class Solution {
    findCircleNum(isConnected: number[][]): number {
        const n = isConnected.length;
        const uf = new UnionFind(isConnected);
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                if (isConnected[i][j] === 1) {
                    uf.union(i, j);
                }
            }
        }
        const findRes = new Set<number>();
        for (let i = 0; i < n; i++) {
            findRes.add(uf.find(i));
        }
        return findRes.size;
    }
}

class UnionFind {
    capital: number[];
    constructor(isConnected: number[][]) {
        this.capital = new Array<number>(isConnected.length);
        for (let i = 0; i < isConnected.length; i++) {
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