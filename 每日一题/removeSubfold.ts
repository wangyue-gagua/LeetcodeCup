/* Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"] */

function removeSubfolders(folder: string[]): string[] {
    // 字典树解法
    const root = new TrieNode();
    const res: string[] = [];
    for (let i = 0; i < folder.length; i++) {
        let word = folder[i].split("/");
        let node = root;
        for (let name of word) {
            if (name === "") continue;
            if (!node.children.has(name)) {
                node.children.set(name, new TrieNode());
            }
            node = node.children.get(name)!;
        }
        node.ref = i;
    }
    const dfs = (cur: TrieNode) => {
        if (cur.ref !== -1) {
            res.push(folder[cur.ref]);
            return;
        }
        for (let [key, value] of cur.children) {
            dfs(value);
        }
    };
    dfs(root);
    return res;
}

class TrieNode {
    ref: number = -1;
    children: Map<string, TrieNode> = new Map();
    constructor() {
        this.children = new Map();
        this.ref = -1;
    }
}

console.log(removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]));
