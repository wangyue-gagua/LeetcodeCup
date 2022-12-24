// 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function (head) {
    if (head === null) {
        return null;
    }
    let cur = head;
    while (cur !== null) {
        let newNode = new Node(cur.val, cur.next, null);
        cur.next = newNode;
        cur = newNode.next;
    }
    cur = head;
    while (cur !== null) {
        if (cur.random !== null) {
            cur.next.random = cur.random.next;
        }
        cur = cur.next.next;
    }
    cur = head;
    let newHead = head.next;
    while (cur !== null) {
        let temp = cur.next;
        cur.next = temp.next;
        if (temp.next !== null) {
            temp.next = temp.next.next;
        }
        cur = cur.next;
    }
    return newHead;
};

var copyRandomList = function (head, cachedNode = new Map()) {
    if (head === null) {
        return null;
    }
    if (!cachedNode.has(head)) {
        cachedNode.set(head, { val: head.val }),
            Object.assign(cachedNode.get(head), {
                next: copyRandomList(head.next, cachedNode),
                random: copyRandomList(head.random, cachedNode),
            });
    }
    return cachedNode.get(head);
};
