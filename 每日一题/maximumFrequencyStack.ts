/* Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7]. */

class FreqStack {
    freqCountMap: Map<number, number>;
    freqStackMap: Map<number, number[]>;
    constructor() {
        this.freqCountMap = new Map<number, number>(); // number出现次数
        this.freqStackMap = new Map<number, number[]>(); // number出现次数对应的number数组
    }

    push(val: number): void {
        if (this.freqCountMap.has(val)) {
            this.freqCountMap.set(val, this.freqCountMap.get(val)! + 1);
        } else {
            this.freqCountMap.set(val, 1);
        }
        const freq = this.freqCountMap.get(val)!
        if (this.freqStackMap.has(freq)) {
            this.freqStackMap.get(freq)!.push(val);
        } else {
            this.freqStackMap.set(freq, [val]);
        }
    }

    pop(): number {
        const freq = this.freqStackMap.size;
        const val = this.freqStackMap.get(freq)!.pop()!;
        this.freqCountMap.set(val, this.freqCountMap.get(val)! - 1);
        if (this.freqStackMap.get(freq)!.length === 0) {
            this.freqStackMap.delete(freq);
        }
        return val;
    }

    prints() {
        console.log(this.freqCountMap);
        console.log(this.freqStackMap);
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * var obj = new FreqStack()
 * obj.push(val)
 * var param_2 = obj.pop()
 */

let obj = new FreqStack();
obj.push(5);
obj.push(7);
obj.push(5);
obj.push(7);
obj.push(4);
obj.push(5);
obj.prints();
console.log(obj.pop());
obj.prints();
console.log(obj.pop());
obj.prints();
console.log(obj.pop());
obj.prints();
console.log(obj.pop());
obj.prints();
