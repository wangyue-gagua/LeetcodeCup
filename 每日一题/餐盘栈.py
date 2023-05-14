""" 我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。

实现一个叫「餐盘」的类 DinnerPlates：

DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。
 

示例：

输入： 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
输出：
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

解释：
DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // 栈的现状为：    2  4
                                    1  3  5
                                    ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 2。栈的现状为：      4
                                          1  3  5
                                          ﹈ ﹈ ﹈
D.push(20);        // 栈的现状为：  20  4
                                   1  3  5
                                   ﹈ ﹈ ﹈
D.push(21);        // 栈的现状为：  20  4 21
                                   1  3  5
                                   ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
                                            1  3  5
                                            ﹈ ﹈ ﹈
D.popAtStack(2);   // 返回 21。栈的现状为：       4
                                            1  3  5
                                            ﹈ ﹈ ﹈ 
D.pop()            // 返回 5。栈的现状为：        4
                                            1  3 
                                            ﹈ ﹈  
D.pop()            // 返回 4。栈的现状为：    1  3 
                                           ﹈ ﹈   
D.pop()            // 返回 3。栈的现状为：    1 
                                           ﹈   
D.pop()            // 返回 1。现在没有栈。
D.pop()            // 返回 -1。仍然没有栈。 """

class DinnerPlates:
    stack = [[] for _ in range(1000000)]
    capacity = 0
    lastNotFull = 0
    rightMost = -1
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lastNotFull = 0
        self.rightMost = -1
        self.stack = [[] for _ in range(1000000)]


    def push(self, val: int) -> None:
        self.stack[self.lastNotFull].append(val)
        if self.lastNotFull > self.rightMost:
            self.rightMost = self.lastNotFull
        # print(self.stack, "push")
        while len(self.stack[self.lastNotFull]) == self.capacity:
            self.lastNotFull += 1


    def pop(self) -> int:
        if self.rightMost < 0:
            return -1
        else:
            val = self.stack[self.rightMost].pop()
            while self.rightMost >= 0 and len(self.stack[self.rightMost]) == 0:
                self.rightMost -= 1
            self.lastNotFull = min(self.lastNotFull, self.rightMost)
            self.lastNotFull = max(self.lastNotFull, 0)
            return val



    def popAtStack(self, index: int) -> int:
        if len(self.stack[index]) == 0:
            return -1
        else:
            val = self.stack[index].pop()
            if index == self.rightMost:
                while len(self.stack[self.rightMost]) == 0:
                    self.rightMost -= 1
            self.lastNotFull = min(self.lastNotFull, index)
            return val



# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

# testObj = DinnerPlates(2)
# testObj.push(1)
# testObj.push(2)
# testObj.push(3)
# testObj.push(4)
# testObj.push(5)
# print(testObj.popAtStack(0))
# testObj.push(20)
# testObj.push(21)
# print(testObj.popAtStack(0))
# print(testObj.popAtStack(2))
# print(testObj.pop())
# print(testObj.pop())
# print(testObj.pop())
# print(testObj.pop())
# print(testObj.pop())

# testObj = DinnerPlates(1)
# testObj.push(1)
# testObj.push(2)
# testObj.popAtStack(1)
# print(testObj.pop())
# testObj.push(1)
# testObj.push(2)
# print(testObj.pop())
# print(testObj.pop())

testObj = DinnerPlates(2)
testObj.push(1)
testObj.push(2)
testObj.push(3)
testObj.push(4)
testObj.push(5)
print(testObj.popAtStack(1))
print(testObj.popAtStack(1))
#print(testObj.pop())
#testObj.push(1)
#testObj.push(2)
#print(testObj.pop())
#print(testObj.pop())