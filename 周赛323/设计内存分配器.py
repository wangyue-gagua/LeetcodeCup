""" 给你一个整数 n ，表示下标从 0 开始的内存数组的大小。所有内存单元开始都是空闲的。

请你设计一个具备以下功能的内存分配器：

分配 一块大小为 size 的连续空闲内存单元并赋 id mID 。
释放 给定 id mID 对应的所有内存单元。
注意：

多个块可以被分配到同一个 mID 。
你必须释放 mID 对应的所有内存单元，即便这些内存单元被分配在不同的块中。
实现 Allocator 类：

Allocator(int n) 使用一个大小为 n 的内存数组初始化 Allocator 对象。
int allocate(int size, int mID) 找出大小为 size 个连续空闲内存单元且位于  最左侧 的块，分配并赋 id mID 。返回块的第一个下标。如果不存在这样的块，返回 -1 。
int free(int mID) 释放 id mID 对应的所有内存单元。返回释放的内存单元数目。
 

示例：

输入
["Allocator", "allocate", "allocate", "allocate", "free", "allocate", "allocate", "allocate", "free", "allocate", "free"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
输出
[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]

解释
Allocator loc = new Allocator(10); // 初始化一个大小为 10 的内存数组，所有内存单元都是空闲的。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 0 。内存数组变为 [1, , , , , , , , , ]。返回 0 。
loc.allocate(1, 2); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,2, , , , , , , , ]。返回 1 。
loc.allocate(1, 3); // 最左侧的块的第一个下标是 2 。内存数组变为 [1,2,3, , , , , , , ]。返回 2 。
loc.free(2); // 释放 mID 为 2 的所有内存单元。内存数组变为 [1, ,3, , , , , , , ] 。返回 1 ，因为只有 1 个 mID 为 2 的内存单元。
loc.allocate(3, 4); // 最左侧的块的第一个下标是 3 。内存数组变为 [1, ,3,4,4,4, , , , ]。返回 3 。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,1,3,4,4,4, , , , ]。返回 1 。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 6 。内存数组变为 [1,1,3,4,4,4,1, , , ]。返回 6 。
loc.free(1); // 释放 mID 为 1 的所有内存单元。内存数组变为 [ , ,3,4,4,4, , , , ] 。返回 3 ，因为有 3 个 mID 为 1 的内存单元。
loc.allocate(10, 2); // 无法找出长度为 10 个连续空闲内存单元的空闲块，所有返回 -1 。
loc.free(7); // 释放 mID 为 7 的所有内存单元。内存数组保持原状，因为不存在 mID 为 7 的内存单元。返回 0 。"""

from typing import Dict, List


class Allocator:
    myMemory = []
    allocatedBlock: Dict[int, List[List[int]]] = {
    }  # mID: [[start1, end1], [start2, end2]]

    def __init__(self, n: int):
        self.myMemory = [0] * n
        self.allocatedBlock = {}

    def allocate(self, size: int, mID: int) -> int:
        if size == 0:
            return -1
        start = 0
        end = 0
        while start < len(self.myMemory):
            if self.myMemory[start] == 0:
                end = start
                while end < len(self.myMemory) and self.myMemory[end] == 0:
                    end += 1
                if end - start >= size:
                    for i in range(start, start + size):
                        self.myMemory[i] = mID
                    if mID not in self.allocatedBlock:
                        self.allocatedBlock[mID] = []
                    self.allocatedBlock[mID].append([start, start + size - 1])
                    return start
                start = end
            else:
                start += 1
        return -1

    def free(self, mID: int) -> int:
        if mID not in self.allocatedBlock:
            return 0
        count = 0
        # print(self.allocatedBlock, self.myMemory)
        for block in self.allocatedBlock[mID]:
            for i in range(block[0], block[1] + 1):
                self.myMemory[i] = 0
                count += 1
        self.allocatedBlock[mID] = []
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)



obj = Allocator(10)
print(obj.allocate(1, 1))
print(obj.allocate(1, 2))
print(obj.allocate(1, 3))
print(obj.free(2))
print(obj.allocate(3, 4))
print(obj.allocate(1, 1))
print(obj.allocate(1, 1))
print(obj.free(1))
print(obj.allocate(10, 2))
print(obj.free(7))

# test2
# ["Allocator","allocate","allocate","free","free"]
# [[7],[3,1],[5,2],[1],[3]]
aother = Allocator(7)
print(aother.allocate(3, 1))
print(aother.allocate(5, 2))
print(aother.free(1))
print(aother.free(3))