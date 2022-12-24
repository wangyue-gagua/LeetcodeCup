/* Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
*/

class LRUCache {
    cache: Map<number, { key: number; value: number }>;
    keyValueList: Map<number, { key: number; value: number }>;
    capacity: number;

    constructor(capacity: number) {
        this.capacity = capacity;
        this.cache = new Map();
        this.keyValueList = new Map();
    }

    get(key: number): number {
        // If the key is not in the cache, return -1.
        if (!this.cache.has(key)) {
            // this.prints();
            return -1;
        }

        // Move the key-value pair to the front of the list to mark it as the
        // most recently used.
        let keyValuePair = this.cache.get(key)!;
        this.keyValueList.delete(keyValuePair?.key);
        this.keyValueList.set(key, { key, value: keyValuePair.value });
        this.cache.set(key, {
            key,
            value: keyValuePair.value,
        });
        // this.prints();
        return keyValuePair.value;
    }

    put(key: number, value: number): void {
        // If the key is already in the cache, update its value and move it to
        // the front of the list to mark it as the most recently used.
        if (this.cache.has(key)) {
            let keyValuePair = this.cache.get(key)!;
            this.keyValueList.delete(keyValuePair?.key);
            this.keyValueList.set(key, { key, value });
            this.cache.set(key, { key, value });
        } else {
            // If the cache is at capacity, remove the least recently used key
            // before inserting the new key.
            if (this.cache.size == this.capacity) {
                let keyValuePair = this.keyValueList.get(
                    this.keyValueList.keys().next().value
                )!;
                this.keyValueList.delete(keyValuePair?.key);
                this.cache.delete(keyValuePair.key);
            }

            // Add the new key-value pair to the front of the list and the cache.
            this.keyValueList.set(key, { key, value });
            this.cache.set(key, { key, value });
        }
        // this.prints();
    }

    prints() {
        console.log(this.cache);
        console.log(this.keyValueList);
    }
}

// ["LRUCache","put","put","get","put","get","get"]
// [[2],[2,1],[1,1],[2],[4,1],[1],[2]]

const LRUobj = new LRUCache(2);
LRUobj.put(2, 1);
LRUobj.put(1, 1);
console.log(LRUobj.get(2));
LRUobj.put(4, 1);
console.log(LRUobj.get(1));
console.log(LRUobj.get(2));

class ConciseLRUCache {
    cache: Map<number, number>;
    capacity: number;

    constructor(capacity: number) {
        this.capacity = capacity;
        this.cache = new Map();
    }

    get(key: number): number {
        // If the key is not in the cache, return -1.
        if (!this.cache.has(key)) {
            // this.prints();
            return -1;
        }

        // Move the key-value pair to the front of the list to mark it as the
        // most recently used.
        const val = this.cache.get(key)!;
        this.cache.delete(key);
        this.cache.set(key, val);
        return val;
    }

    put(key: number, value: number): void {
        // If the key is already in the cache, update its value and move it to
        // the front of the list to mark it as the most recently used.
        if (this.cache.has(key)) {
            this.cache.delete(key);
        } else {
            // If the cache is at capacity, remove the least recently used key
            // before inserting the new key.
            if (this.cache.size == this.capacity) {
                this.cache.delete(this.cache.keys().next().value);
            }
            // Add the new key-value pair to the front of the list and the cache.
        }
        this.cache.set(key, value);
        // this.prints();
    }

    prints() {
        console.log(this.cache);
    }
}
