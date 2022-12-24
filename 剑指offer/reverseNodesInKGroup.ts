/* Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed. */

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

 function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    if (k === 1) return head;
    let dummy = new ListNode(0, head);
    let prev = dummy;
    let cur = head;
    let count = 0;
    while (cur) {
        count++;
        if (count % k === 0) {
            prev = reverse(prev, cur.next);
            cur = prev.next;
        } else {
            cur = cur.next;
        }
    }
    return dummy.next;

};

function reverse(prev: ListNode, next: ListNode | null): ListNode {
    let last = prev.next;
    let cur = last.next;
    while (cur !== next) {
        last.next = cur.next;
        cur.next = prev.next;
        prev.next = cur;
        cur = last.next;
    }
    return last;
}