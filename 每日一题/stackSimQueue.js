var CQueue = function() {
    const stack1 = []
    const stack2 = []
    this.stack1 = stack1
    this.stack2 = stack2
};

/** 
 * @param {number} value
 * @return {void}
 */
CQueue.prototype.appendTail = function(value) {
    while (this.stack2.length > 0) {
        this.stack1.push(this.stack2.pop())
    }
    this.stack1.push(value)
};

/**
 * @return {number}
 */
CQueue.prototype.deleteHead = function() {
    while (this.stack1.length > 0) {
        this.stack2.push(this.stack1.pop())
    }
    if (this.stack2.length === 0) {
        return -1
    } else {
        return this.stack2.pop()
    }

};

/**
 * Your CQueue object will be instantiated and called as such:
 * var obj = new CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */