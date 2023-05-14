/* Design a data structure that efficiently finds the majority element of a given subarray.

The majority element of a subarray is an element that occurs threshold times or more in the subarray.

Implementing the MajorityChecker class:

MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] that occurs at least threshold times, or -1 if no such element exists.
 

Example 1:

Input
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
Output
[null, 1, -1, 2]

Explanation
MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2
 

Constraints:

1 <= arr.length <= 2 * 104
1 <= arr[i] <= 2 * 104
0 <= left <= right < arr.length
threshold <= right - left + 1
2 * threshold > right - left + 1
At most 104 calls will be made to query. */

class MajorityChecker {
    // 2 * threshold > right - left + 1 故在当前长度区间内, 有且只有一个元素可能出现次数超过threshold
    // 前缀和记录到当前位置的元素出现次数 23/32 空间超时
    // 直接暴力吧 31/32 超出时间限制
    selfArr: number[]
    selfAllReadySearched: Map<string, number> = new Map<string, number>()
    constructor(arr: number[]) {
        this.selfArr = arr;
    }

    query(left: number, right: number, threshold: number): number {
        const queryKey = `${left}-${right}-${threshold}`;
        if (this.selfAllReadySearched.has(queryKey)) {
            return this.selfAllReadySearched.get(queryKey)!;
        }
        const len = right - left + 1;
        const map = new Map<number, number>();
        for (let i = left; i <= right; i++) {
            const item = this.selfArr[i];
            if (map.has(item)) {
                map.set(item, map.get(item)! + 1);
            } else {
                map.set(item, 1);
            }
        }
        for (const [key, value] of map.entries()) {
            if (value >= threshold) {
                this.selfAllReadySearched.set(queryKey, key);
                return key;
            }
        }
        this.selfAllReadySearched.set(queryKey, -1);
        return -1;
    }
}

/**
 * Your MajorityChecker object will be instantiated and called as such:
 * var obj = new MajorityChecker(arr)
 * var param_1 = obj.query(left,right,threshold)
 */

const myObj = new MajorityChecker([1, 1, 2, 2, 1, 1]);
console.log(myObj.query(0, 5, 4));
console.log(myObj.query(0, 3, 3));
console.log(myObj.query(2, 3, 2));